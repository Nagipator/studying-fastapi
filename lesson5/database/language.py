from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base_meta import BaseSQLAlchemyModel


class Language(BaseSQLAlchemyModel):
    __tablename__ = "language"

    id = Column(Integer, primary_key=True, autoincrement=True)
    lng = Column(String, nullable=False)

    users = relationship("UserLanguage",  back_populates="language")

    def __str__(self):
        return f"Language(id={self.id}, lng='{self.lng}')"

    def __repr__(self):
        return str(self)  # self.__str__()
