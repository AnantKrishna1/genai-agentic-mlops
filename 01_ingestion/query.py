from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.llms import Ollama
from app.config import CHROMA_DB_DIR

# Load vector store
embedding_model = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
vectordb = Chroma(persist_directory=str(CHROMA_DB_DIR), embedding_function=embedding_model)

# LLM
llm = Ollama(model="mistral")  # You can change to llama2, gemma, etc.

# Prompt Template (optional for RAG)
template = """
Use the following context to answer the question.
If you don't know the answer, say "I don't know" – don't make up an answer.

Context:
{context}

Question: {question}
Answer:
"""
prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=template,
)

# RAG Chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectordb.as_retriever(),
    chain_type="stuff",
    chain_type_kwargs={"prompt": prompt},
    return_source_documents=True
)

# Ask a question
query = input("Ask a question about the PDF: ")
response = qa_chain(query)

print("\nAnswer:\n", response["result"])

# Optional: Print source chunk(s)
print("\nSources:\n")
for doc in response["source_documents"]:
    print(doc.page_content[:300])  # Print first 300 characters
    print("="*80)