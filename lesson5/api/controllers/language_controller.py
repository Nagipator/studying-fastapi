from typing import Optional, List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from starlette import status

from database import session_factory, Language, get_session
from model import LanguageIn, LanguageOut
from services import LanguageService

router = APIRouter(prefix="/language", tags=["language"])


@router.get("/{id}", response_model=Optional[LanguageOut])
async def get_language(language_id: int,
                       session: AsyncSession = Depends(get_session)):
    language = await LanguageService.get_language_by_id(language_id, session)
    if language:
        dto_language = LanguageOut(**language.to_dict())
        return dto_language
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Language with id {language_id} not found!")


@router.get("/", response_model=List[LanguageOut])
async def get_languages(session: AsyncSession = Depends(get_session)):
    languages = await LanguageService.get_all_languages(session)
    return list(map(lambda x: LanguageOut(**x.to_dict()), languages))


@router.post("/", response_model=LanguageOut)
async def create_language(language_dto: LanguageIn,
                          session: AsyncSession = Depends(get_session)):
    new_language = await LanguageService.create_language(language_dto,
                                                         session)
    return LanguageOut(**new_language.to_dict())


@router.put("/", response_model=LanguageOut)
async def update_language(language_dto: LanguageOut,
                          session: AsyncSession = Depends(get_session)):
    language = await LanguageService.get_language_by_id(language_dto.id, session)
    if language:
        language.update(language_dto.model_dump(exclude={"id"}))
        await session.commit()
        return LanguageOut(**language.to_dict())

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Language with id {language_dto.id} not found!")


@router.delete("/")
async def delete_language(language_id: int,
                          session: AsyncSession = Depends(get_session)):
    language = await LanguageService.get_language_by_id(language_id, session)
    if language:
        await session.delete(language)
        await session.commit()
        return {"status": "OK"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Language with id {language_id} not found!")


