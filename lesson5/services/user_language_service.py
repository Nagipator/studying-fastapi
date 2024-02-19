from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from lesson5.database import UserLanguage
from lesson5.model import UserLanguageModel


class UserLanguageService:
    @staticmethod
    async def get_user_language_by_user_id(user_id: int, session: AsyncSession) -> List[UserLanguage]:
        query = await session.execute(select(UserLanguage).where(UserLanguage.user_id == user_id))
        user_language = query.scalars().all()
        return user_language

    @staticmethod
    async def get_user_language_by_dto(user_id: int, language_id: int,
                                       session: AsyncSession) -> Optional[UserLanguage]:
        query = await session.execute(select(UserLanguage).where(UserLanguage.user_id == user_id)
                                      .where(UserLanguage.language_id == language_id))
        user_language = query.scalars().first()
        return user_language

    @staticmethod
    async def create_user_language(dto_user_language: UserLanguageModel, session: AsyncSession) -> UserLanguage:
        user_language = UserLanguage(**dto_user_language.model_dump())
        session.add(user_language)
        await session.commit()
        return user_language
