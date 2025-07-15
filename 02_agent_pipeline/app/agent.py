# app/agent.py

from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOllama
from app.tools import tools
from app.memory import memory

# ✅ Define required prompt with both 'input' and 'agent_scratchpad'
prompt = PromptTemplate.from_template("""
You are an intelligent agent that helps users answer questions or perform tasks.
Use the tools available to you if needed.

Question: {input}

{agent_scratchpad}
""")

# ✅ Initialize LLM and Agent
llm = ChatOllama(model="mistral")
agent = create_openai_functions_agent(llm=llm, tools=tools, prompt=prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, memory=memory, verbose=True)
