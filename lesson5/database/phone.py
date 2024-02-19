from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base_meta import Base, BaseSQLAlchemyModel


class Phone(BaseSQLAlchemyModel):
    __tablename__ = "phone"

    id = Column(Integer, primary_key=True, autoincrement=True)
    phone_number = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))

    user = relationship("User", back_populates="phones")


    def __str__(self):
        return f"Phone(id={self.id}, phone_number='{self.phone_number}', user_id={self.user})"

    def __repr__(self):
        return str(self)  # self.__str__()
