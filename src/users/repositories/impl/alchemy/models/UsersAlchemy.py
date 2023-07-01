from sqlalchemy import Column, String, Integer
from src.common.infrastructure.BaseAlchemyModel import Base


__all__ = ['UsersAlchemy']


class UsersAlchemy(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    firstname = Column(String, nullable=False)
    middlename = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
