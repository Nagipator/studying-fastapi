from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base_meta import Base, BaseSQLAlchemyModel


class UserLanguage(BaseSQLAlchemyModel):
    __tablename__ = "user_language"

    language_id = Column(ForeignKey("language.id"), primary_key=True)
    user_id = Column(ForeignKey("user.id"), primary_key=True)

    language = relationship("Language", back_populates="users")
    user = relationship("User", back_populates="languages")

