# chatbot_agent.py

from app.agent import agent_executor

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    result = agent_executor.invoke({"input": user_input})
    print("🤖 Agent:", result["output"])
