from fastapi import FastAPI
from backend.routes import router

app = FastAPI(title="Travel Safety Companion API")

app.include_router(router)
