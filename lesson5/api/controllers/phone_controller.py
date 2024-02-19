from typing import Optional, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from lesson5.database import get_session
from lesson5.model import PhoneOut, PhoneIn
from lesson5.services import PhoneServices

router = APIRouter(prefix="/phone", tags=["phone"])


@router.get("/{id}", response_model=Optional[PhoneOut])
async def get_phone(phone_id: int, session: AsyncSession = Depends(get_session)):
    phone = await PhoneServices.get_phone_by_id(phone_id, session)
    if phone:
        dto_phone = PhoneOut(**phone.to_dict())
        return dto_phone
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"""Phone with id {phone_id} not found!""")


@router.get("/", response_model=List[PhoneOut])
async def get_phones(session: AsyncSession = Depends(get_session)):
    phones = await PhoneServices.get_phones(session)
    return list(map(lambda x: PhoneOut(**x.to_dict()), phones))


@router.post("/", response_model=PhoneOut)
async def create_phone(dto_phone: PhoneIn, session: AsyncSession = Depends(get_session)):
    phone = await PhoneServices.create_phone(session, dto_phone)
    return PhoneOut(**phone.to_dict())


@router.delete("/")
async def delete_phone(phone_id: int, session: AsyncSession = Depends(get_session)):
    phone = await PhoneServices.get_phone_by_id(phone_id, session)
    if phone:
        await session.delete(phone)
        await session.commit()
        raise HTTPException(status_code=status.HTTP_200_OK, detail="The phone was successfully deleted")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Phone with id {phone_id} not found!")
