# 💳 Project 15: Financial Pipeline Dashboard (Raspberry Pi 5)

> **Context**: Automated financial statement parser, transaction categorizer, SQLite database store, and portfolio NAV tracker.  
> **Status**: 🟢 **Production / Tested**  
> **Host**: Raspberry Pi 5 (`192.168.1.92`)  
> **Repository**: [`deepshah08/raspberry-pi-5-ecosystem/projects/15-financial-pipeline`](https://github.com/deepshah08/raspberry-pi-5-ecosystem/tree/main/projects/15-financial-pipeline)  

---

## 1. Key Components

- **Portfolio Tracker (`portfolio_tracker.py`)**: Ingests buy/sell transactions from CSV/brokerages, calculates real-time Net Asset Value (NAV), and generates percentage asset allocations.
- **Statement Parser (`parse_statements.py`)**: Extracts transaction dates, merchant descriptions, and amounts from statements into SQLite/Postgres.

## 2. Verified Functionality & Test Suite

- `projects/15-financial-pipeline/tests/test_financial_pipeline.py`: Validates portfolio NAV calculations, asset allocation percentages, regex statement parsing, and database transactions.
- **Test Results**: 2/2 passing tests.
