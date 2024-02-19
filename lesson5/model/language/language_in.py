from typing import List, Dict

from pydantic import BaseModel


class LanguageIn(BaseModel):
    lng: str

    class Config:
        orm_mode: True


if __name__ == "__main__":
    lng = LanguageIn(lng='123')
