from llama_index.llms.groq import Groq
from llama_index.core import Settings
from .llmParent import Placeholder

class GroqModel(Placeholder):

    """Defines a model using the Groq API. In this case, only the api key and model settings are needed"""
    def __init__(self, api_key, model, temperature, max_tokens):
        super().__init__(api_key, model, temperature, max_tokens)

        self.llm_model = Settings
        self.llm_model.llm = Groq(model=self.model, api_key=self.api_key)

    def ask_model(self, chat):
        resp = self.llm_model.llm.complete(chat)
        return resp
    
    def get_model(self):
        return self.llm_model.llm
    