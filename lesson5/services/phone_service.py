from typing import Optional, List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from lesson5.database import Phone
from lesson5.model import PhoneIn


class PhoneServices:
    @staticmethod
    async def get_phone_by_id(phone_id: int, session: AsyncSession) -> Optional[Phone]:
        query = await session.execute(select(Phone).where(Phone.id == phone_id))
        phone = query.scalars().first()
        return phone

    @staticmethod
    async def get_phones(session: AsyncSession) -> List[Phone]:
        query = await session.execute(select(Phone).order_by(Phone.id))
        phones = query.scalars().all()
        return phones

    @staticmethod
    async def create_phone(session: AsyncSession, dto_phone: PhoneIn) -> Phone:
        phone = Phone(**dto_phone.model_dump())
        session.add(phone)
        await session.commit()
        return phone
