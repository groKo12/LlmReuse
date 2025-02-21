"""This file is an abstract parent of an LLM. This allows the calling application to 
vary the model being called"""

class Placeholder():
    """This file is an abstract parent of an LLM. This allows the calling application to 
vary the model being called"""
    def __init__(self,
            api_key,
            model,
            temperature,
            max_tokens
            ):
        self.api_key = api_key
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
    
    def ask_model(self, chat: str):
        """Queries the Llm"""
        pass

    def get_model(self):
        """Returns the model type"""
        pass

