from .user_in import UserIn


class UserOut(UserIn):
    id: int

    class Config:
        orm_mode: True
