from llama_index.llms import ollama as ol
from llama_index.core import Settings
from .llmParent import Placeholder

class OllamaModel(Placeholder):
    """Creates a class of Ollama models for the intent of abstraction"""

    def __init__(self, 
                 api_key, 
                 model, 
                 temperature, 
                 max_tokens, 
                 timeout
                 ):
        super().__init__(api_key, 
                         model, 
                         temperature, 
                         max_tokens
                         )

        self.llm_model = Settings
        self.llm_model.llm = ol.Ollama(model=model, temperature=temperature, request_timeout=timeout)

    # Ask the model a question directly
    def ask_model(self, chat):
        resp = self.llm_model.llm.complete(chat)
        return resp

    # Return Raw instance of the model
    def get_model(self):
        return self.llm_model.llm
