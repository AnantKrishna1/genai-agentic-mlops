# app/utils.py

def print_thoughts(state):
    print("\n--- Agent Trace ---")
    for step in state['steps']:
        print(f"\n🔹 Input: {step['input']}")
        print(f"🔸 Output: {step['output']}")
        print(f"🧠 Tool Used: {step['tool']} | Observation: {step['observation']}")
    print("\n====================\n")
