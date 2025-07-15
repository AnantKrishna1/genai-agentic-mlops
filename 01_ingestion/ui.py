# ui.py

import streamlit as st
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.llms import Ollama
from app.config import CHROMA_DB_DIR

# 🔧 Fix Windows Path issue
import pathlib
if isinstance(CHROMA_DB_DIR, pathlib.Path):
    CHROMA_DB_DIR = str(CHROMA_DB_DIR)

# Initialize vector DB and LLM
embedding_model = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
vectordb = Chroma(persist_directory=CHROMA_DB_DIR, embedding_function=embedding_model)
retriever = vectordb.as_retriever()
llm = Ollama(model="mistral")

# Create the Retrieval QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

# Streamlit app layout
st.set_page_config(page_title="📄 GenAI Chat with PDF", layout="wide")
st.title("💬 GenAI RAG Chatbot")
st.markdown("Ask questions about the ingested PDF document below.")

query = st.text_input("Ask a question:")

if query:
    with st.spinner("Generating answer..."):
        response = qa_chain(query)
        st.success(response["result"])

        # Show sources
        with st.expander("🔍 Sources"):
            for i, doc in enumerate(response["source_documents"]):
                st.markdown(f"**Source {i+1}:**")
                st.markdown(doc.page_content[:500])  # Show first 500 characters
