from fastapi import FastAPI
from routes import base, data
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import get_settings
from contextlib import asynccontextmanager

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    app.mongo_connection = AsyncIOMotorClient(settings.MONGODB_URL)
    app.db_client = app.mongo_connection[settings.MONGODB_DATABASE]
    yield
    app.mongo_connection.close()

app = FastAPI(lifespan=lifespan)

app.include_router(base.base_router)
app.include_router(data.data_router)