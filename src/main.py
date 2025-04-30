from fastapi import FastAPI
from routes import base, data
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import get_settings
import logging
logger = logging.getLogger('uvicorn.error')


app = FastAPI()

@app.on_event("startup")
async def start_db_client():
    settings = get_settings()
    app.mongo_connection = AsyncIOMotorClient(settings.MONGODB_URL)
    app.db_client = app.mongo_connection[settings.MONGODB_DATABASE]
    # Fix: call command() on the database object, not on a collection
    await app.db_client.command('ping')
    logger.info("Connected to MongoDB Successfully")

    
@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongo_connection.close()

app.include_router(base.base_router)
app.include_router(data.data_router)
