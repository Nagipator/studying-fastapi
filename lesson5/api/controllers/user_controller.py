from typing import Optional, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from lesson5.database import get_session
from lesson5.model import UserOut, UserIn
from lesson5.services import UserService

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/{id}", response_model=Optional[UserOut])
async def get_user(user_id: int, session: AsyncSession = Depends(get_session)):
    user = await UserService.get_user_by_id(user_id, session)
    if user:
        dto_user = UserOut(**user.to_dict())
        return dto_user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"""User with id {user_id} not found!""")


@router.get("/", response_model=List[UserOut])
async def get_users(session: AsyncSession = Depends(get_session)):
    users = await UserService.get_users(session)
    dto_users = list(map(lambda x: UserOut(**x.to_dict()), users))
    return dto_users


@router.post("/", response_model=UserOut)
async def create_user(dto_user: UserIn, session: AsyncSession = Depends(get_session)):
    user = await UserService.create_user(dto_user, session)
    return UserOut(**user.to_dict())


@router.put("/", response_model=UserOut)
async def update_user(dto_user: UserOut, session: AsyncSession = Depends(get_session)):
    user = await UserService.get_user_by_id(dto_user.id, session)
    if user:
        user.update(dto_user.model_dump(exclude={"id"}))
        await session.commit()
        return UserOut(**user.to_dict())
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"""User with id {dto_user.id} not found!""")


@router.delete("/")
async def delete_user(user_id: int, session: AsyncSession = Depends(get_session)):
    user = await UserService.get_user_by_id(user_id, session)
    if user:
        await session.delete(user)
        await session.commit()
        raise HTTPException(status_code=status.HTTP_200_OK, detail=f"""The user was successfully deleted""")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"""User with id {user_id} not found!""")

