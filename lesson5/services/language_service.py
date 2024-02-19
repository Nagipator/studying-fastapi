from typing import Optional, List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import Language
from model import LanguageIn


class LanguageService:
    @staticmethod
    async def get_language_by_id(language_id: int,
                                 session: AsyncSession) -> Optional[Language]:
        query = await session.execute(select(Language).where(Language.id == language_id))
        language = query.scalars().first()
        return language

    @staticmethod
    async def get_all_languages(session: AsyncSession) -> List[Language]:
        query = await session.execute(select(Language).order_by(Language.id))
        languages = query.scalars().all()
        return languages

    @staticmethod
    async def create_language(language_dto: LanguageIn,
                              session: AsyncSession) -> Language:
        langauge = Language(**language_dto.model_dump())
        session.add(langauge)
        await session.commit()
        return langauge
