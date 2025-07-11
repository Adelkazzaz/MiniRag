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
        
    def process_text(self, text: str):
        return text[:self.default_input_max_charcters].strip()
        
    def generate_text(self, prompt: str, chat_hestory: list = [],
                      max_output_tokens: int=None,
                      temperature: float = None):
        
        if not self.client:
            self.logger.error("OpenAI client is not initialized.")
            return None
        if not self.generation_model_id:
            self.logger.error("Generation model id for OpenAI is not set.")
            return None
        
        max_output_tokens = max_output_tokens if max_output_tokens else self.default_generation_max_output_tokens
        temperature = temperature if temperature else self.default_generation_temperature
        
        chat_hestory.append(
            self.construct_prompt(prompt=prompt, role=OpenAIEnums.USER.value)
        )
        
        completion = self.client.chat.completions.create(
            model = self.generation_model_id,
            messages = chat_hestory,
            max_tokens = max_output_tokens,
            temperature = temperature
        )
        
        if not completion or not completion.choices or len(completion.choices) == 0 or not completion.choices[0].message:
            self.logger.error(f"OpenAI Failed to generate text")
            return None
        
        return completion.choices[0].message["content"] 
    
    
    def embed_text(self, text: str, document_type: str = None):
        if not self.client:
            self.logger.error("OpenAI client is not initialized.")
            return None
        if not self.embedding_model_id:
            self.logger.error("OpenAI Embedding model is not set.")
            return None
        response = self.client.embeddings.create(
            model = self.embedding_model_id,
            input = text,
        )
        
        if not response.data or len(response.data) == 0 or not hasattr(response.data[0], 'embedding'):
            self.logger.error(f"OpenAI Failed to generate embedding for text")
            return None
        
        return response.data[0].embedding
    
    def construct_prompt(self, prompt: str, role: str):
        return {
            "role": role,
            "content": self.process_text(prompt)
        }
        