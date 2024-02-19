from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base_meta import BaseSQLAlchemyModel


class User(BaseSQLAlchemyModel):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=True)
    last_name = Column(String, nullable=False)

    phones = relationship("Phone", back_populates="user")
    languages = relationship("UserLanguage", back_populates="user")

    def __str__(self):
        return f"User(id={self.id}, full_name='{self.first_name + ' ' + self.last_name}')"

    def __repr__(self):
        return str(self)

