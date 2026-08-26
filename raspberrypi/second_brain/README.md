# 🧠 Project 02: Git-Backed Second Brain (Raspberry Pi 5)

> **Context**: Continuous document ingestion, text chunking, and ChromaDB vector search triggered automatically by Gitea/Obsidian git push webhooks.  
> **Status**: 🟢 **Production / Tested**  
> **Host**: Raspberry Pi 5 (`192.168.1.92`)  
> **Repository**: [`deepshah08/raspberry-pi-5-ecosystem/projects/02-second-brain`](https://github.com/deepshah08/raspberry-pi-5-ecosystem/tree/main/projects/02-second-brain)  

---

## 1. Architecture Overview

```mermaid
flowchart TD
    Obsidian["Obsidian / Markdown Notes"] --> GitPush["Git Push to Self-Hosted Gitea"]
    GitPush --> Hook["post-receive Git Hook"]
    Hook --> Ingest["ingest.py (PyPDF, Text, Markdown)"]
    Ingest --> Chunker["Sliding Window Chunker (chunk_text)"]
    Chunker --> Chroma["Persistent ChromaDB Store (/chroma_db)"]
    
    SearchQuery["Semantic Search Query"] --> SearchAPI["search.py / Web Endpoint"]
    SearchAPI --> Chroma
    Chroma --> Results["Ranked Relevant Excerpts & File Metadata"]
```

## 2. Key Components

- **Ingestion Engine (`ingest.py`)**: Scans `.md`, `.txt`, and `.pdf` files, slices into overlapping chunks, and adds batches to ChromaDB.
- **Search Module (`search.py`)**: Performs cosine distance vector search with optional extension filters.
- **Git Hook (`post-receive`)**: Triggers automated indexing upon any push to the SecondBrain repository.

## 3. Verified Functionality & Test Suite

- `projects/02-second-brain/tests/test_second_brain.py`: Validates multi-format ingestion, chunking boundary edge cases, and filtered semantic search.
- **Test Results**: 3/3 passing tests.
