from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.v1.notes import router as notes_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(notes_router, prefix="/api/v1/notes", tags=["Notes"])

@app.get("/healthcheck")
async def health_check():
    """Простой эндпоинт для проверки жизнеспособности сервиса"""
    return {"status": "ok", "message": "Service is running"}
