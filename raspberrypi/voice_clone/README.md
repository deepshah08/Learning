# 🗣️ Project 06: Voice Clone TTS Sandbox (Raspberry Pi 5)

> **Context**: Local text-to-speech sandbox and voice cloning engine for audiobook narration, morning briefing podcasts, and AI voice responses.  
> **Status**: 🟢 **Production / Tested**  
> **Host**: Raspberry Pi 5 (`192.168.1.92`)  
> **Repository**: [`deepshah08/raspberry-pi-5-ecosystem/projects/06-voice-clone`](https://github.com/deepshah08/raspberry-pi-5-ecosystem/tree/main/projects/06-voice-clone)  

---

## 1. Architecture & Components

- **Synthesis Engine (`voice_clone.py`)**: Modular TTS synthesizer supporting reference speaker cloning (`xtts_v2`) with graceful CPU fallback.
- **Audio Output**: Direct stream generation to WAV format for integration with podcasts and morning briefing generators.

## 2. Verified Functionality & Test Suite

- `projects/06-voice-clone/tests/test_voice_clone.py`: Tests synthesis pipeline, output file creation, and missing file exception handling.
- **Test Results**: 2/2 passing tests.
