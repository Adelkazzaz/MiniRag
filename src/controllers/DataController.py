from .BaseController import BaseController
from .ProjectController import ProjectController
from fastapi import UploadFile
from models import ResponseSignal

class DataController(BaseController):
    def __init__(self):
        super().__init__()
        
        self.size_scale = 1048576
        
    def validate_upload_file(self, file: UploadFile):
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False , ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value
        
        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            return False , ResponseSignal.MAX_FILE_SIZE_EXCEEDED.value
        
        return True , ResponseSignal.FILE_VALIDATED_SUCCESS.value
    
    def generate_unique_filename(self, orig_file_name: str, project_id: str):
        random_file_name = self.generate_random_string()
        project_path = ProjectController().get_project_path(project_id=project_id)
        
    def get_clean_file_name():
        pass