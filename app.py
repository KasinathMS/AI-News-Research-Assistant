from fastapi import FastAPI
from pydantic import BaseModel

from rag_pipeline import build_rag_pipeline

app = FastAPI()


class QueryRequest(BaseModel):
    topic: str
    question: str


@app.get("/")
def home():
    return {"message": "AI News Research Assistant Running"}


@app.post("/ask")
def ask_question(request: QueryRequest):

    retriever, llm = build_rag_pipeline(request.topic)

    docs = retriever.invoke(request.question)

    context = "\n".join(
        [doc.page_content[:500] for doc in docs]
    )

    prompt = f"""
    Answer the question based on the context below.

    Context:
    {context}

    Question:
    {request.question}
    """

    answer = llm.invoke(prompt)

    return {
        "topic": request.topic,
        "question": request.question,
        "answer": answer
    }