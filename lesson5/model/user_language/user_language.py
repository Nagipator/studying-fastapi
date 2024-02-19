from pydantic import BaseModel


class UserLanguageModel(BaseModel):
    language_id: int
    user_id: int

    class Config:
        orm_mode: True