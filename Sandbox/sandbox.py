from LlmAbstraction.ollamaModel import OllamaModel as olm
from LlmAbstraction.groq import GroqModel as grq
from dotenv import load_dotenv
from llama_index.core.agent import ReActAgent
import os

load_dotenv()
GROQ_KEY = os.getenv('GROQ_API_KEY')
MODEL = os.getenv("MODEL")

# Instantiate model
test = grq(model=MODEL, api_key=GROQ_KEY, temperature=1, max_tokens=2048)

# Instantiate agent using model
agent = ReActAgent.from_tools(tools=[], llm=test.get_model(), verbose=True)

# Query Agent
text = "How are you?"
resp = agent.chat(text)
print(resp)
