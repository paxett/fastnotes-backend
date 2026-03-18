from sqlalchemy.orm import Mapped, mapped_column
from ..database import Base
from datetime import datetime,timezone
from sqlalchemy import func

class Note(Base):
    __tablename__ = "notes"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    content: Mapped[str] = mapped_column(default="")
    created_at: Mapped[datetime] = mapped_column(server_default=func.text("TIMEZONE('utc', now())"))
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), 
        onupdate=func.text("TIMEZONE('utc', now())")
    )
