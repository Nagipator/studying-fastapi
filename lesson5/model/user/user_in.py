from pydantic import BaseModel


class UserIn(BaseModel):
    first_name: str
    middle_name: str
    last_name: str

    class Config:
        orm_mode: True