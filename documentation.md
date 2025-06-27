## 1. Copy the Documentation

Copy the documentation text below:

---

# LocalAIAgentWithRAG Documentation

## Overview

This project is an AI-powered question-answering system for a pizza restaurant. It uses LangChain, Ollama, and Chroma to retrieve relevant customer reviews and generate expert answers to user questions.

---

## File: `vector.py`

### Purpose

- Loads restaurant review data from a CSV file.
- Embeds the reviews using Ollama embeddings.
- Stores/retrieves document vectors using Chroma.
- Exposes a retriever object for semantic search.

### How It Works

1. **Data Loading**
   - Loads `realistic_restaurant_reviews.csv` from the script directory using pandas.

2. **Embeddings**
   - Initializes an embedding model (`OllamaEmbeddings`) for vectorizing text.

3. **Vector Store**
   - Checks if a Chroma database exists.
   - If not, creates document objects from the CSV and adds them to the database.
   - Always initializes the Chroma vector store.

4. **Retriever**
   - Exposes a retriever that can fetch the top 5 most relevant reviews for a query.

---

## File: main.py

### Purpose

- Loads environment variables and initializes the language model.
- Defines a prompt template for answering pizza restaurant questions.
- Uses the retriever to fetch relevant reviews.
- Runs an interactive loop for user Q&A.

### How It Works

1. **Setup**
   - Loads environment variables from `.env`.
   - Gets the Ollama model name (default: `llama3.2:latest`).
   - Initializes the Ollama language model.

2. **Prompt Template**
   - Defines a prompt that includes relevant reviews and the user's question.

3. **Chain**
   - Chains the prompt and model for easy invocation.

4. **Interactive Loop**
   - Prompts the user for questions.
   - Uses the retriever to fetch relevant reviews.
   - Passes reviews and the question to the model.
   - Prints the model's answer.
   - Exits on "q".

---

## Usage

1. Place `realistic_restaurant_reviews.csv` in the same directory as the scripts.
2. Run `vector.py` once to initialize the vector store (if not already present).
3. Run main.py to start the interactive Q&A session.

---

## Dependencies

- Python 3.8+
- pandas
- langchain
- langchain_ollama
- langchain_chroma
- python-dotenv

---

## Converting to PDF

1. Paste this documentation into a Markdown (`.md`) or Word (`.docx`) file.
2. Open with your preferred editor (VS Code, Word, Google Docs).
3. Export or print as PDF.

