# 🤖 Agentic AI + MLOps Pipeline with LangChain, Ollama, and MLflow

A production-ready, end-to-end pipeline that combines **Agentic AI workflows** and **modern MLOps practices** using **LangChain**, **Ollama**, **ChromaDB**, **MLflow**, and **Streamlit**.

This project supports intelligent PDF-based assistants using RAG (Retrieval-Augmented Generation), tool-based agents, evaluation, logging, and a beautiful UI.

---

## 🧠 Key Features

- 🔍 PDF Ingestion + Chroma Vector Store  
- 🤖 RAG-based QA with Ollama LLMs (Mistral, LLaMA2, etc.)  
- 🧠 Agentic Pipeline with LangGraph + Tools + Memory  
- 📊 LLM Monitoring with MLflow  
- 🧪 Evaluation with cosine similarity scoring  
- 🖼️ Streamlit Chatbot UI  
- 🐳 Dockerized for deployment  

---

## 📁 Project Structure

├── 01_ingestion/ # Load PDF → Chunk → Embed → Store
│ ├── app/
│ │ ├── config.py
│ │ ├── ingest.py
│ │ └── utils.py
│ ├── data/ # Holds raw PDFs
│ ├── embeddings/ # ChromaDB vector index
│ ├── query.py # Simple RAG-based QA
│ ├── ui.py # Streamlit chatbot
│ └── requirements.txt
│
├── 02_agent_pipeline/ # Agentic reasoning pipeline
│ ├── app/
│ │ ├── chatbot_agent.py # LangGraph + Tools + Memory
│ │ └── test_agent.py
│ └── requirements.txt
│
├── 06_monitoring_mlflow/ # LLM monitoring + logging
│ ├── log_utils.py
│ ├── track_run.py
│ ├── requirements.txt
│ └── mlruns/ # Auto-generated MLflow run logs
│
├── 07_evaluation/ # RAG response evaluation
│ ├── eval_config.yaml
│ ├── evaluate_rag.py
│ ├── evaluation_utils.py
│ └── requirements.txt
│
├── Dockerfile # Streamlit + Ollama Docker config
└── README.md # You’re reading it!


---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/AnantKrishna1/genai-agentic-mlops.git
cd genai-agentic-mlops

2. (Optional) Create a virtual environment

conda create -n genai-rag python=3.10 -y
conda activate genai-rag

3. Install base requirements

pip install -r 01_ingestion/requirements.txt

4. Run Ollama model (e.g. Mistral)

ollama run mistral

🔄 Workflow: Step-by-Step
📥 PDF Ingestion & Vector Store
Copy your PDF:

cp sample.pdf 01_ingestion/data/

Run embedding pipeline:

cd 01_ingestion/app
python ingest.py

✅ Output: Document is split, embedded using SentenceTransformer, and stored in ChromaDB.

💬 Query with RAG
cd ..
python query.py

✅ Ask questions like:

What is the main purpose of the PDF?

🌐 Streamlit Chatbot UI

streamlit run ui.py

✅ An interactive chatbot (powered by Ollama + RAG) will launch in your browser.

🧠 Agentic Pipeline with LangGraph

cd ../02_agent_pipeline/
python app/chatbot_agent.py

✅ Features:

LangGraph-powered memory chain

Tools (Calculator, File Reader, DuckDuckGo Search)

Contextual reasoning over PDF

📈 LLM Monitoring with MLflow

cd ../06_monitoring_mlflow/
python track_run.py

✅ Tracks:

Prompt and response

Latency

Similarity metrics

Accuracy

View logs:
mlflow ui

✅ Evaluation & Benchmarking
cd ../07_evaluation/
python evaluate_rag.py

✅ Performs:

Cosine similarity scoring

Latency measurement

Pass/Fail based on eval_config.yaml

🐳 Docker Deployment
Build the Docker image:

docker build -t genai-chatbot .

Run the container:
docker run -p 8501:8501 genai-chatbot

⚙️ Optional: Run Ollama container (Mistral)
docker run -d -p 11434:11434 ollama/ollama mistral

🔹 Question: What is the main goal of the document?
📤 Model Answer: The document aims to test the ingestion pipeline in an Agentic AI + MLOps project.
✅ Expected: The document is for testing the ingestion pipeline...
⏱️ Response Time: 2.7 seconds
📊 Similarity Score: 0.87
🟢 PASSED

🧰 Technologies Used
Category	Tools & Libraries
LLMs	Mistral (via Ollama), LLaMA2, Gemma
Vector DB	ChromaDB + SentenceTransformers
Frameworks	LangChain, LangGraph
Monitoring	MLflow
Frontend	Streamlit
Deployment	Docker

