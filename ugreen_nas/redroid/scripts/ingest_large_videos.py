#!/usr/bin/env python3
"""
Hardened Video Ingestion & Segmentation Pipeline for Google Photos ReDroid
- Integrates with centralized rate_limiter.py on UGREEN NAS
- Granular per-part checkpointing (resumes exactly from interrupted part)
- Zero leftover temporary files (cleans slices and extracted tar files)
- Lossless keyframe stream copy (< 1.8 GB chunks to bypass 32-bit ashmem ceiling)
- Asynchronous, deterministic SQLite WAL cloud verification (Zero ADB / Screencaps)
"""
import os
import sys
import time
import math
import json
import argparse
import subprocess

DF_DIR = '/mnt/media-storage/DF'
TAR_FILE = f'{DF_DIR}/wedding_archive_DF.tar'
STAGING_DIR = f'{DF_DIR}/staging_flat'
STATE_FILE = f'{DF_DIR}/fenil_processed_batches.txt'
LOG_FILE = f'{DF_DIR}/fenil_ingest.log'
NAS_HOST = 'Deep Shah@192.168.1.80'
NAS_STAGING = '/volume2/docker/redroid/inbox_staging'
NAS_INBOX = '/volume2/docker/redroid/inbox'
LIMITER_PATH = '/volume2/docker/redroid/scripts/rate_limiter.py'

def log(msg):
    line = f'[{time.strftime("%Y-%m-%d %H:%M:%S")}] {msg}'
    print(line, flush=True)
    try:
        with open(LOG_FILE, 'a') as f:
            f.write(line + '\n')
    except Exception:
        pass

def get_processed():
    if not os.path.exists(STATE_FILE):
        return set()
    with open(STATE_FILE) as f:
        return set(line.strip() for line in f if line.strip())

def mark_processed(item):
    with open(STATE_FILE, 'a') as f:
        f.write(f'{item}\n')
    log(f'Checkpoint committed for {item}.')

def check_nas_rate_limit(size_bytes):
    try:
        res = subprocess.run(
            ['ssh', '-o', 'BatchMode=yes', NAS_HOST, f'python3 "{LIMITER_PATH}" check {size_bytes}'],
            capture_output=True, text=True
        )
        return res.returncode == 0
    except Exception as e:
        log(f'Warning: Could not contact rate limiter on NAS: {e}')
        return True

def record_nas_upload(size_bytes):
    try:
        subprocess.run(
            ['ssh', '-o', 'BatchMode=yes', NAS_HOST, f'python3 "{LIMITER_PATH}" record {size_bytes}'],
            capture_output=True, text=True
        )
    except Exception as e:
        log(f'Warning: Could not record upload to rate limiter: {e}')

def wait_for_google_photos(filename):
    log(f'Waiting for Google Photos cloud confirmation for {filename} via SQLite WAL...')
    cmd = [
        'ssh', '-o', 'BatchMode=yes', NAS_HOST,
        f'sudo /volume2/docker/redroid/scripts/verify_backup.py wait "{filename}" --timeout 600 --interval 3'
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode == 0:
        try:
            out = proc.stdout.strip()
            if "{" in out:
                json_part = out[out.find("{"):out.rfind("}")+1]
                data = json.loads(json_part)
                media_key = data.get("cloud_media_key", "UNKNOWN")
                log(f'Verified: {filename} uploaded to Google Photos cloud! Cloud Key: {media_key}')
                return
        except Exception as e:
            log(f'Verified exit code 0 for {filename} (JSON parse note: {e})')
            return
    else:
        log(f'Warning: Verification failed (rc={proc.returncode}): {proc.stderr}')
        raise RuntimeError(f'Upload verification failed for {filename}')

REMAINING_VIDEOS = [
    ('DF/Videos/Traditional/Welcome-003.mp4', 'Welcome-003.mp4'),
    ('DF/Videos/Traditional/Wedding-001.mp4', 'Wedding-001.mp4'),
    ('DF/Videos/Traditional/Sangeet-002.mp4', 'Sangeet-002.mp4')
]

def main():
    parser = argparse.ArgumentParser(description="Wedding Video Ingestion Worker")
    parser.add_argument("--burst", action="store_true", help="Override 1GB rate limit for burst ingestion")
    parser.add_argument("--cooling-seconds", type=int, default=30, help="Pause seconds between uploaded parts")
    args = parser.parse_args()

    os.makedirs(STAGING_DIR, exist_ok=True)
    processed = get_processed()

    # Pre-mark Welcome-003_Part1 if not already marked
    if 'Welcome-003_Part1.mp4' not in processed:
        mark_processed('Welcome-003_Part1.mp4')
        processed.add('Welcome-003_Part1.mp4')

    log('========================================================')
    log(f'Starting Video Ingestion Pipeline (Burst Override: {args.burst})')
    log('========================================================')

    for rel_path, item_name in REMAINING_VIDEOS:
        if item_name in processed:
            log(f'Skipping already fully processed video: {item_name}')
            continue

        log('--------------------------------------------------------')
        log(f'Processing Large Video: {item_name}')
        log('--------------------------------------------------------')

        full_video_path = os.path.join(DF_DIR, rel_path)
        extracted_from_tar = False
        if not os.path.exists(full_video_path):
            log(f'Extracting {item_name} from master TAR on SMR drive...')
            subprocess.check_call(['tar', '-xf', TAR_FILE, '-C', DF_DIR, rel_path])
            extracted_from_tar = True

        size_bytes = os.path.getsize(full_video_path)
        size_gb = size_bytes / (1024**3)
        log(f'Video {item_name} size: {size_gb:.2f} GB ({size_bytes} bytes)')

        # Probe duration
        probe_cmd = ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', full_video_path]
        dur = float(subprocess.check_output(probe_cmd).decode().strip())
        log(f'Duration: {dur:.1f}s ({dur/60:.1f} minutes)')

        # Split into chunks strictly < 1.75 GB to safely respect 32-bit ashmem limits (< 2.0 GiB)
        num_parts = max(2, int(math.ceil(size_bytes / (1.75 * 1024**3))))
        part_dur = dur / num_parts
        log(f'Dividing into {num_parts} parts (~{size_gb/num_parts:.2f} GB / {part_dur/60:.1f} min each) using lossless stream copy...')

        base_name = os.path.splitext(item_name)[0]
        all_parts_successful = True

        for p_idx in range(num_parts):
            part_filename = f'{base_name}_Part{p_idx+1}.mp4'
            if part_filename in processed:
                log(f'Skipping already uploaded part: {part_filename}')
                continue

            # Check rate limiter unless burst flag is active
            part_est_bytes = int(size_bytes / num_parts)
            if not args.burst:
                if not check_nas_rate_limit(part_est_bytes):
                    log(f'Daily upload rate limit reached on NAS! Pausing at {part_filename} until next window or --burst flag.')
                    all_parts_successful = False
                    return

            start_t = p_idx * part_dur
            part_local_path = os.path.join(STAGING_DIR, part_filename)

            log(f'Generating Part {p_idx+1}/{num_parts}: {part_filename} (start: {start_t:.1f}s, dur: {part_dur:.1f}s)...')
            split_cmd = ['ffmpeg', '-y', '-ss', str(start_t), '-t', str(part_dur), '-i', full_video_path, '-c', 'copy', part_local_path]
            subprocess.check_call(split_cmd, stderr=subprocess.DEVNULL)

            part_actual_size = os.path.getsize(part_local_path)
            part_size_mb = part_actual_size / (1024*1024)
            log(f'Part {p_idx+1} ready ({part_size_mb:.1f} MB). Streaming to NAS staging...')

            stream_cmd = f'tar -cf - -C "{STAGING_DIR}" "{part_filename}" | ssh -o BatchMode=yes "{NAS_HOST}" "mkdir -p {NAS_STAGING} && tar -xf - -C {NAS_STAGING}"'
            subprocess.check_call(stream_cmd, shell=True)
            os.remove(part_local_path)

            log(f'Atomically moving {part_filename} to NAS inbox (safe against & and special characters)...')
            mv_cmd = [
                'ssh', '-o', 'BatchMode=yes', NAS_HOST,
                f"find '{NAS_STAGING}' -mindepth 1 -maxdepth 1 -exec mv -t '{NAS_INBOX}' {{}} +"
            ]
            subprocess.check_call(mv_cmd)

            log('Waiting for NAS inotify daemon to ingest into ReDroid DCIM...')
            poll = 0
            while True:
                out = subprocess.check_output([
                    'ssh', '-o', 'BatchMode=yes', NAS_HOST,
                    f"find '{NAS_INBOX}' -mindepth 1 -maxdepth 1 -type f 2>/dev/null | wc -l"
                ]).decode().strip()
                inbox_count = int(out or 0)
                if inbox_count == 0:
                    log(f'NAS inbox drained to 0. {part_filename} ingested into ReDroid!')
                    break
                time.sleep(5)
                poll += 1
                if poll > 40:
                    log(f'Warning: Inbox drain wait reached timeout (200s). Proceeding to cloud verification...')
                    break

            wait_for_google_photos(part_filename)
            record_nas_upload(part_actual_size)
            mark_processed(part_filename)
            processed.add(part_filename)
            log(f'Part {p_idx+1}/{num_parts} successfully uploaded and recorded to cloud!')

            if p_idx < num_parts - 1:
                log(f'Cooling interval ({args.cooling_seconds}s) to preserve organic upload pacing...')
                time.sleep(args.cooling_seconds)

        if all_parts_successful:
            mark_processed(item_name)
            log(f'Finished all {num_parts} parts for {item_name}!')
            if extracted_from_tar and os.path.exists(full_video_path):
                log(f'Purging extracted temporary video file {full_video_path} (master TAR preserved)...')
                os.remove(full_video_path)

    log('==========================================================')
    log('INGESTION PIPELINE RUN COMPLETED!')
    log('==========================================================')

if __name__ == '__main__':
    main()
