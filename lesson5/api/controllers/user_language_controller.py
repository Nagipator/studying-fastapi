from typing import Optional, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from lesson5.database import get_session
from lesson5.model import UserLanguageModel
from lesson5.services.user_language_service import UserLanguageService

router = APIRouter(prefix="/user_language", tags=["user_language"])


@router.get("/{user_id}", response_model=List[UserLanguageModel])
async def get_all_user_language(user_id: int, session: AsyncSession = Depends(get_session)):
    all_user_language = await UserLanguageService.get_user_language_by_user_id(user_id, session)
    dto_user_language = list(map(lambda x: UserLanguageModel(**x.to_dict()), all_user_language))
    return dto_user_language


@router.get("/", response_model=Optional[UserLanguageModel])
async def get_user_language(user_id: int, language_id: int, session: AsyncSession = Depends(get_session)):
    user_language = await UserLanguageService.get_user_language_by_dto(user_id, language_id, session)
    if user_language:
        return UserLanguageModel(**user_language.to_dict())
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"""User with id = {user_id} does`t know language with id = {language_id} """)


@router.post("/", response_model=UserLanguageModel)
async def create_user_language(dto_user_language: UserLanguageModel, session: AsyncSession = Depends(get_session)):
    user_language = await UserLanguageService.create_user_language(dto_user_language, session)
    return UserLanguageModel(**user_language.to_dict())


@router.delete("/")
async def delete_user_language(dto_user_language: UserLanguageModel, session: AsyncSession = Depends(get_session)):
    user_language = await UserLanguageService.get_user_language_by_dto(dto_user_language.user_id,
                                                                       dto_user_language.language_id,
                                                                       session)
    if user_language:
        await session.delete(user_language)
        await session.commit()
        raise HTTPException(status_code=status.HTTP_200_OK, detail="The user_language was successfully deleted")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"""The user_language with user_id = {dto_user_language.user_id} and \
language_id = {dto_user_language.language_id} not found!""")
