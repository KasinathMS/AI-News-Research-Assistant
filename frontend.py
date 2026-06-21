import streamlit as st
import requests

st.title("AI News Research Assistant")


# Topic input
category = st.text_input("Enter News Topic")


# Question input
question = st.text_area("Ask Your Question")


if st.button("Get Answer"):

    payload = {
        "topic": category,
        "question": question
    }

    response = requests.post(
        "http://127.0.0.1:8000/ask",
        json=payload
    )

    data = response.json()

    st.subheader("Answer")
    st.write(data["answer"])