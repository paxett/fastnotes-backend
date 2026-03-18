from app.database import async_session
from app.config import settings
from app.models.user import User
from app.core.security import hash_password
from sqlalchemy import select
import asyncio

async def create_first_superuser():
    async with async_session() as session:
        result = await session.execute(
            select(User).filter(User.email == settings.SUPERUSER_EMAIL)
        )
        user = result.scalar_one_or_none()

        if not user:
            new_user = User(
                email=settings.SUPERUSER_EMAIL,
                hashed_password=hash_password(settings.SUPERUSER_PASSWORD),
                is_superuser=True
            )
            session.add(new_user)
            await session.commit()
            print("Superuser created!")

if __name__ == "__main__":
    asyncio.run(create_first_superuser())
