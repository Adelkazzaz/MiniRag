from ..LLMInterface import LLMInterface
from ..LLMEnums import OpenAIEnums
from openai import OpenAI
import logging

class OpenAIProvider(LLMInterface):
    
    def __init__(self, api_key: str,
                       api_url: str = None,
                       default_input_max_charcters: int = 500,
                       default_generation_max_tokens: int = 1000,
                       default_temperature: float = 0.2,):
        
        self.api_key = api_key
        self.client = OpenAI(api_key)
        self.api_url = api_url
        self.default_input_max_charcters = default_input_max_charcters
        self.default_generation_max_tokens = default_generation_max_tokens
        self.default_temperature = default_temperature
        self.logger = logging.getLogger(__name__)
        