from .language_in import LanguageIn


class LanguageOut(LanguageIn):
    id: int

    class Config:
        orm_mode: True
