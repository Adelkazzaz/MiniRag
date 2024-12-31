from fastapi import FastAPI, APIRouter, Depends, UploadFile
from helpers.config import get_settings, Settings 
import os

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["rag_v1", "data"],
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str,file: UploadFile
                      app_settings: Settings = Depends(get_settings)):
    
    app_name = app_settings.APP_NAME
    app_version = app_settings.APP_VERSION
    return {"app_name": app_name,
            "app_version": app_version,
    }
