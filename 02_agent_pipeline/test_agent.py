from app.agent import chain

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    result = chain.invoke({"input": user_input})
    print("🤖 Agent:", result["output"])
