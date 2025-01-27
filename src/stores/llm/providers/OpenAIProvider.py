from ..LLMInterface import LLMInterface
from ..LLMEnums import OpenAIEnums
from openai import OpenAI
import logging

class OpenAIProvider(LLMInterface):
    
    def __init__(self, api_key: str,
                       api_url: str = None,
                       default_input_max_charcters: int = 500,
                       default_generation_max_output_tokens: int = 1000,
                       default_generation_temperature: float = 0.2,):
        
        self.api_key = api_key
        self.api_url = api_url
        
        self.default_input_max_charcters = default_input_max_charcters
        self.default_generation_max_output_tokens = default_generation_max_output_tokens
        self.default_generation_temperature = default_generation_temperature
        
        self.generation_model_id = None
        
        self.embedding_model_id = None
        self.embedding_size = None
        
        self.client = OpenAI(
            api_key = self.api_key,
            api_url = self.api_url
        )
        
        self.logger = logging.getLogger(__name__)
        
        
    def set_generation_model(self, model_id: str):
        self.generation_model_id = model_id
        
    def set_embedding_model(self, model_id: str, embedding_size: int):
        self.embedding_model_id = model_id
        self.embedding_size = embedding_size
        
    def generate_text(self, prompt: str, max_output_tokens: int, temperature: float = None):
        raise NotImplementedError("OpenAIProvider.generate_text() is not implemented yet.")
    
    def embed_text(self, text: str, document_type: str):
        if not self.client:
            self.logger.error("OpenAI client is not initialized.")
            return None
        if not self.embedding_model_id:
            self.logger.error("Embedding model is not set.")
            return None
        response = self.client.embeddings.create(
            model = self.embedding_model_id,
            input = text,
        )
        
        if response.status_code != 200 or not response.data or len(response.data) == 0 or not response.data[0].get("embedding"):
            self.logger.error(f"OpenIA Failed to embedding text: {response.text}")
            return None
        
        return response.data[0].get("embedding")