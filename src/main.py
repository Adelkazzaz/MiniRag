from fastapi import FastAPI
from routes import base # type: ignore


app=FastAPI()
app.include_router(base.base_router)