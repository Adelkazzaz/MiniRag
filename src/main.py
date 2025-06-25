from fastapi import FastAPI
from routes import base, data
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import get_settings
from .stores.llm.LLMProviderFactory import LLMProviderFactory
import logging
logger = logging.getLogger('uvicorn.error')


app = FastAPI()

async def start_db_client():
    settings = get_settings()
    app.mongo_connection = AsyncIOMotorClient(settings.MONGODB_URL)
    app.db_client = app.mongo_connection[settings.MONGODB_DATABASE]
    await app.db_client.command('ping')
    logger.info("Connected to MongoDB Successfully")
    
    llm_provider_factory = LLMProviderFactory(settings)
    app.generation_client = llm_provider_factory.create(provider=settings.GENERATION_PROVIDER)
    app.generation_client.set_generation_model(model_id=settings.GENERATION_MODEL_ID)
    app.embedding_client = llm_provider_factory.create(provider=settings.EMBEDDING_PROVIDER)
    app.embedding_client.set_embedding_model(model_id=settings.EMBEDDING_MODEL_ID,
                                             embedding_size=settings.EMBEDDING_MODEL_SIZE)
    
async def shutdown_db_client():
    app.mongo_connection.close()

app.router.lifespan.on_startup.append(start_db_client)
app.router.lifespan.on_shutdown.append(shutdown_db_client)

app.include_router(base.base_router)
app.include_router(data.data_router)
