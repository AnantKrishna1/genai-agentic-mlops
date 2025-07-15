from langchain.llms import Ollama
import mlflow

# Start MLflow run
mlflow.start_run()

# Initialize LLM (Ollama must be running locally)
llm = Ollama(model="mistral")

# Log model parameter
mlflow.log_param("model_name", "mistral")

# Make a test call
prompt = "What is the capital of France?"
response = llm.invoke(prompt)

# Print response
print("LLM Response:", response)

# Log output as a metric or simple string artifact
mlflow.log_metric("response_length", len(response))
mlflow.log_text(response, "response.txt")

# End run
mlflow.end_run()
