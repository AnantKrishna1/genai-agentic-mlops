import time
from langchain.vectorstores import Chroma
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import Ollama
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import numpy as np

# Load embedding model
embedding_model = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# Load vector store
vectordb = Chroma(persist_directory="../01_ingestion/embeddings", embedding_function=embedding_model)

# Load LLM
llm = Ollama(model="mistral")

# Create QA chain
qa = RetrievalQA.from_chain_type(llm=llm, retriever=vectordb.as_retriever())

# Load evaluation model (same as embedding model for cosine similarity)
evaluator = SentenceTransformer("all-MiniLM-L6-v2")

# Define test questions and expected answers
test_cases = [
    {
        "question": "What is the main goal of the document?",
        "expected": "The document is for testing the ingestion pipeline in an agentic AI + MLOps project."
    },
    {
        "question": "What kind of text does the sample PDF contain?",
        "expected": "Plain text to be extracted, chunked, and embedded."
    }
]

# Evaluate each test case
for case in test_cases:
    query = case["question"]
    expected = case["expected"]

    print(f"\n🔹 Question: {query}")

    # Track response time
    start = time.time()
    result = qa.run(query)
    end = time.time()

    print(f"📤 Model Answer: {result}")
    print(f"✅ Expected: {expected}")
    print(f"⏱️ Response Time: {round(end - start, 2)} seconds")

    # Cosine similarity
    result_vec = evaluator.encode([result])[0]
    expected_vec = evaluator.encode([expected])[0]
    score = cosine_similarity([result_vec], [expected_vec])[0][0]
    print(f"📊 Similarity Score: {round(score, 2)}")

    if score > 0.8:
        print("🟢 PASSED\n")
    else:
        print("🔴 FAILED\n")
