from .phone_in import PhoneIn


class PhoneOut(PhoneIn):
    id: int

    class Config:
        orm_mode: True
