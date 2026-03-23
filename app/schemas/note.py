from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class NoteCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=50, description="Заголовок заметки")
    content: Optional[str] = Field(default="", max_length=1000, description="Текст заметки")

class NoteUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=50)
    content: Optional[str] = Field(None, max_length=1000) 

class NoteResponse(NoteCreate):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class PaginationMeta(BaseModel):
    total: int
    limit: int
    offset: int

class NoteListResponse(BaseModel):
    items: list[NoteResponse]
    pagination: PaginationMeta