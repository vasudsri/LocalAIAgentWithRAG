# LocalAIAgentWithRAG

This project implements a local AI agent with Retrieval-Augmented Generation (RAG) capabilities. It processes local documents, stores their embeddings, and uses an LLM to answer user queries with context retrieved from a vector database.

## Features
- Converts and ingests local documents (e.g., CSV, markdown, PDF)
- Stores document embeddings in a local Chroma vector database
- Uses RAG to provide context-aware answers from an LLM
- Interactive command-line or API interface

## Requirements
- Python 3.8+
- The following Python packages:
  - chromadb
  - langchain
  - langchain_ollama (or other LLM integration)
  - python-dotenv
  - (and any other dependencies listed in `requirements.txt`)

Install dependencies with:
```bash
pip install -r requirements.txt
```

## Usage
1. Place your data files (e.g., `realistic_restaurant_reviews.csv`) in the project directory.
2. (Optional) Set environment variables in a `.env` file as needed.
3. Run the main script:
   ```bash
   python main.py
   ```
4. The script will ingest data, store embeddings, and allow you to ask questions interactively or via API.

## Project Structure
- `main.py` - Main entry point for the RAG agent
- `vector.py` - Vector database and embedding logic
- `chrome_langchain_db/` - Local Chroma vector database files
- `README.md` - Project documentation

## Notes
- The default data and database paths can be changed in `main.py` and `vector.py`.
- Extend the project by adding new data loaders or LLM integrations as needed.

## License
See [LICENSE](../LICENSE) for details.
