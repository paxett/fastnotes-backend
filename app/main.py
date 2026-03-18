from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.v1.notes import router as notes_router
from app.api.v1.users import router as users_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(notes_router, prefix="/api/v1/notes", tags=["Notes"])
app.include_router(users_router, prefix="/api/v1/users", tags=["Users"])

@app.get("/healthcheck")
async def health_check():
    """Простой эндпоинт для проверки жизнеспособности сервиса"""
    return {"status": "ok", "message": "Service is running"}
