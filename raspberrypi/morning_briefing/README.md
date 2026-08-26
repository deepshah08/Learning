# 🌅 Project 16: Morning Briefing Generator (Raspberry Pi 5)

> **Context**: Autonomous daily digest synthesizer merging news headlines, market sentiment scores, and tasks into structured daily markdown and audio briefings.  
> **Status**: 🟢 **Production / Tested**  
> **Host**: Raspberry Pi 5 (`192.168.1.92`)  
> **Repository**: [`deepshah08/raspberry-pi-5-ecosystem/projects/16-morning-briefing`](https://github.com/deepshah08/raspberry-pi-5-ecosystem/tree/main/projects/16-morning-briefing)  

---

## 1. Key Components

- **Briefing Generator (`main.py`)**: Ingests RSS news feeds, combines with real-time market sentiment indicators, and compiles structured markdown digests saved to the media vault (`/mnt/nas/media_vault`).
- **Systemd Automation (`morning-briefing.service / .timer`)**: Executes daily at 06:00 AM.

## 2. Verified Functionality & Test Suite

- `projects/16-morning-briefing/tests/test_morning_briefing.py`: Validates markdown briefing generation, title extraction, sentiment inclusion, and file writing.
- **Test Results**: 2/2 passing tests.
