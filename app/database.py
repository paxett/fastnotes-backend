from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from app.config import settings

# Движок для асинхронных запросов
engine = create_async_engine(settings.DATABASE_URL)

# Фабрика сессий (как "курьер", который носит данные в базу)
async_session = async_sessionmaker(engine, expire_on_commit=False)

# Базовый класс для всех будущих моделей (таблиц)
class Base(DeclarativeBase):
    pass

# Зависимость для эндпоинтов FastAPI
async def get_db():
    async with async_session() as session:
        yield session
