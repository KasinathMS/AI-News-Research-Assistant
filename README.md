# AI News Research Assistant

An AI-powered Retrieval-Augmented Generation (RAG) application that retrieves the latest news articles on a user-specified topic and answers natural language questions using Llama 3.2.

## Features

- Fetches real-time news articles using NewsAPI
- Retrieves topic-specific news based on user input
- Uses semantic search with FAISS and Hugging Face embeddings
- Generates context-aware answers using Llama 3.2 via Ollama
- FastAPI backend for processing requests
- Streamlit frontend for interactive question answering

## Tech Stack

- Python
- FastAPI
- Streamlit
- LangChain
- FAISS
- Hugging Face Embeddings
- Ollama (Llama 3.2)
- NewsAPI

## Project Structure

```text
AI-News-Research-Assistant/
│
├── app.py              # FastAPI backend
├── frontend.py         # Streamlit frontend
├── rag_pipeline.py     # RAG pipeline implementation
├── fetch_news.py       # News retrieval using NewsAPI
├── .env                # API keys
├── requirements.txt
└── README.md
```

## Workflow

```text
User Question
      │
      ▼
Streamlit Frontend
      │
      ▼
FastAPI Backend
      │
      ▼
Fetch Latest News (NewsAPI)
      │
      ▼
Text Chunking
      │
      ▼
Generate Embeddings
      │
      ▼
Store in FAISS
      │
      ▼
Retrieve Relevant Context
      │
      ▼
Llama 3.2 (Ollama)
      │
      ▼
Generated Answer
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI-News-Research-Assistant.git
cd AI-News-Research-Assistant
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file and add:

```env
NEWS_API_KEY=your_newsapi_key
```

### 5. Install and Run Ollama

Pull the Llama 3.2 model:

```bash
ollama pull llama3.2:1b
```

Start Ollama:

```bash
ollama serve
```

## Running the Application

### Start FastAPI Backend

```bash
uvicorn app:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

### Start Streamlit Frontend

```bash
streamlit run frontend.py
```

## Example Usage

1. Enter a news topic (e.g., Artificial Intelligence, Machine Learning, Cybersecurity).
2. Ask a question related to the selected topic.
3. The system retrieves relevant news articles and generates an answer using Llama 3.2.

### Example

**Topic**

```text
Artificial Intelligence
```

**Question**

```text
What are the latest developments in AI?
```

**Output**

```text
AI-generated answer based on the latest retrieved news articles.
```
