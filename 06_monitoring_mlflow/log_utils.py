 import mlflow

def log_prompt_and_response(prompt: str, response: str, model_name: str = "mistral"):
    with mlflow.start_run():
        mlflow.set_tag("model", model_name)
        mlflow.log_param("prompt", prompt)
        mlflow.log_param("response", response)
        mlflow.log_metric("response_length", len(response))
        print("✅ Logged to MLflow")

