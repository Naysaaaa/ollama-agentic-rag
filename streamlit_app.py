import streamlit as st

from app.core.llm import llm
from app.agents.retriever import retrieve_documents

st.set_page_config(
    page_title="Agentic AI Research Assistant",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Agentic AI Research Assistant")
st.caption(
    "Powered by Ollama, FAISS, LangChain and RAG"
)

st.write(
    "Ask questions from your uploaded PDF documents."
)

question = st.text_input(
    "Enter your question"
)

if question:

    results = retrieve_documents(question)

    if not results:
        st.error("Answer not found in uploaded documents.")
        st.stop()

    best_score = results[0][1]

    # Adjust threshold if needed
    THRESHOLD = 0.7

    if best_score > THRESHOLD:
        st.warning("Answer not found in uploaded documents.")
        st.stop()

    docs = [doc for doc, score in results]

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are an expert document assistant.

Answer the user's question ONLY using the context below.

If the context contains relevant information,
provide a detailed answer.

Only say:
'Answer not found in uploaded documents.'

when the context clearly does not contain the answer.

Context:
{context}

Question:
{question}

Answer:
"""

    with st.spinner("Generating answer..."):
        response = llm.invoke(prompt)

    st.subheader("Answer")
    st.write(response.content)

    with st.expander("Retrieved Chunks"):
        for i, (doc, score) in enumerate(results, start=1):
            st.write(f"Chunk {i}")
            st.write(f"Similarity Score: {score}")
            st.write(doc.page_content[:1000])
            st.divider()