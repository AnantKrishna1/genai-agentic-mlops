# app/ingest.py

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings
from config import DATA_DIR, CHROMA_DB_DIR

# Load your PDF
pdf_path = DATA_DIR / "sample.pdf"
loader = PyPDFLoader(str(pdf_path))
pages = loader.load()

# Split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = splitter.split_documents(pages)

# Embed chunks
embedding_model = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
db = Chroma.from_documents(chunks, embedding_model, persist_directory=str(CHROMA_DB_DIR))

# Save DB
db.persist()
print(f"✅ Ingested and stored {len(chunks)} chunks.")
