from helpers.config import get_settings, Settings 
import random, string
import os

class BaseDataModel:
    def __init__(self, db_client: str):
        self.db_client = db_client
        self.app_settings: Settings  = get_settings()