# 📈 Project 14: Market Sentiment Tracker (Raspberry Pi 5)

> **Context**: Automated financial news RSS scraper and sentiment analyzer using VADER intensity scores and local Ollama model integration with historical JSON logging.  
> **Status**: 🟢 **Production / Tested**  
> **Host**: Raspberry Pi 5 (`192.168.1.92`)  
> **Repository**: [`deepshah08/raspberry-pi-5-ecosystem/projects/14-market-sentiment`](https://github.com/deepshah08/raspberry-pi-5-ecosystem/tree/main/projects/14-market-sentiment)  

---

## 1. Key Components

- **Sentiment Analyzer (`sentiment_analyzer.py`)**: Parses financial RSS feeds (Yahoo Finance, CNBC) and scores compound sentiment using VADER and deterministic lexicon fallbacks.
- **Report Generator**: Records daily scores to `/mnt/nas/ai_models/sentiment_history.json` for trending and Morning Briefing integration.

## 2. Verified Functionality & Test Suite

- `tests/test_sentiment.py`: Validates RSS fetching, compound sentiment averaging, daily report saving, and directory path handling.
- **Test Results**: 5/5 passing tests.
