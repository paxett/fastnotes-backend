from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
from typing import List
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .note import Note

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    is_superuser: Mapped[bool] = mapped_column(
        default=False,
        server_default="false",
        nullable=False
    )

    notes: Mapped[List["Note"]] = relationship("Note", back_populates="owner", cascade="all, delete-orphan")

