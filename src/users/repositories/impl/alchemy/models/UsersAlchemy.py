from sqlalchemy import Column, String
from fastapi_utils.guid_type import GUID
from src.common.infrastructure.BaseAlchemyModel import Base


__all__ = ['UsersAlchemy']


class UsersAlchemy(Base):
    __tablename__ = 'users'
    guid = Column(GUID, primary_key=True)
    firstname = Column(String, nullable=False)
    middlename = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
