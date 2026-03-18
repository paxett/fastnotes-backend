from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List

# Импортируем из соседних папок
from app.database import get_db
from app.models.note import Note
from app.schemas.note import NoteCreate, NoteResponse, NoteUpdate

router = APIRouter()

# Создание заметки (POST)
@router.post("/", response_model=NoteResponse)
async def create_note(note_data: NoteCreate, db: AsyncSession = Depends(get_db)):
    new_note = Note(**note_data.model_dump())
    db.add(new_note)
    await db.commit()
    await db.refresh(new_note)
    return new_note

# Получение всех заметок (GET)
@router.get("/", response_model=List[NoteResponse])
async def get_notes(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Note))
    return result.scalars().all()

# Получение заметки по ID
@router.get("/{note_id}", response_model=NoteResponse)
async def get_note(note_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Note).filter(Note.id == note_id))
    note = result.scalar_one_or_none()
    
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    
    return note

# Удаление заметки по ID
@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_note(note_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Note).filter(Note.id == note_id))
    note = result.scalar_one_or_none()
    
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    
    # Удаляем и фиксируем изменения
    await db.delete(note)
    await db.commit()
    
    # Возвращаем пустой ответ (стандарт для DELETE)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# Апдейт заметки
@router.patch("/{note_id}", response_model=NoteResponse)
async def update_note(
        note_id: int,
        note_data: NoteUpdate,
        db: AsyncSession = Depends(get_db)
):
    # Ищем существующую заметку
    result = await db.execute(select(Note).filter(Note.id == note_id))
    note = result.scalar_one_or_none()

    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    # Обновляем только те поля, которые прислал пользователь
    # exclude_unset=True проигнорирует поля, которые остались None в схеме
    update_data = note_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(note, key, value)

    # Сохраняем и отдаем обновленный объект
    await db.commit()
    await db.refresh(note)
    return note
