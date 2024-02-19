from pydantic import BaseModel


class PhoneIn(BaseModel):
    phone_number: str
    user_id: int

    class Config:
        orm_mode: True
