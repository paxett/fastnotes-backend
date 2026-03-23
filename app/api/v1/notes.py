from fastapi import APIRouter, Depends, HTTPException, status, Response, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from app.api import get_db, get_current_user, apply_user_filter
from app.models import Note
from app.schemas import NoteCreate, NoteResponse, NoteUpdate, NoteListResponse
from app.models.user import User
from app.core import constants

router = APIRouter()

# Создание заметки (POST)
@router.post("/", response_model=NoteResponse)
async def create_note(
        note_data: NoteCreate,
        db: AsyncSession = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    new_note = Note(
        **note_data.model_dump(),
        owner_id=current_user.id
    )
    db.add(new_note)
    await db.commit()
    await db.refresh(new_note)
    return new_note

# Получение всех заметок (GET)
@router.get("/", response_model=NoteListResponse)
async def get_notes(
        offset: int = Query(0, ge=0),
        limit: int = Query(10, ge=1, le=100),
        db: AsyncSession = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    count_query = (apply_user_filter(select(func.count()), current_user))
    count_result = await db.execute(count_query)
    count = int(count_result.scalar_one())

    notes_query = (apply_user_filter(select(Note), current_user)
             .offset(offset)).limit(limit).order_by(Note.id.desc())
    notes_result = await db.execute(notes_query)
    notes = notes_result.scalars().all() or 0

    return {
        "items": notes,
        "pagination": {
            "total": count,
            "limit": limit,
            "offset": offset
        }
    }

# Получение заметки по ID
@router.get("/{note_id}", response_model=NoteResponse)
async def get_note(
        note_id: int,
        db: AsyncSession = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    query = apply_user_filter(select(Note), current_user).filter(Note.id == note_id)
    result = await db.execute(query)
    note = result.scalar_one_or_none()

    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=constants.NOTE_NOT_FOUND)

    return note

# Удаление заметки по ID
@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_note(
        note_id: int,
        db: AsyncSession = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    query = apply_user_filter(select(Note), current_user).filter(Note.id == note_id)
    result = await db.execute(query)
    note = result.scalar_one_or_none()

    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=constants.NOTE_NOT_FOUND)

    await db.delete(note)
    await db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

# Апдейт заметки
@router.patch("/{note_id}", response_model=NoteResponse)
async def update_note(
        note_id: int,
        note_data: NoteUpdate,
        db: AsyncSession = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    query = apply_user_filter(select(Note), current_user).filter(Note.id == note_id)
    result = await db.execute(query)
    note = result.scalar_one_or_none()

    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=constants.NOTE_NOT_FOUND)

    update_data = note_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(note, key, value)

    await db.commit()
    await db.refresh(note)
    return note