from typing import Optional, List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from lesson5.database import User
from lesson5.model import UserIn


class UserService:
    @staticmethod
    async def get_user_by_id(user_id: int, session: AsyncSession) -> Optional[User]:
        query = await session.execute(select(User).where(User.id == user_id))
        user = query.scalars().first()
        return user

    @staticmethod
    async def get_users(session: AsyncSession) -> List[User]:
        query = await session.execute(select(User).order_by(User.id))
        users = query.scalars().all()
        return users

    @staticmethod
    async def create_user(dto_user: UserIn, session: AsyncSession) -> User:
        user = User(**dto_user.model_dump())
        session.add(user)
        await session.commit()
        return user
