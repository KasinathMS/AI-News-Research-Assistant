from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM

from fetch_news import fetch_news


def build_rag_pipeline(topic):

    # Fetch latest news
    news_articles = fetch_news(topic)

    # Split text into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    documents = splitter.create_documents(news_articles)

    # Create embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Store embeddings in FAISS
    vector_store = FAISS.from_documents(documents, embeddings)

    # Create retriever
    retriever = vector_store.as_retriever(
    search_kwargs={"k": 4}
    )
    
    llm = OllamaLLM(model="llama3.2:1b")
    return retriever, llm