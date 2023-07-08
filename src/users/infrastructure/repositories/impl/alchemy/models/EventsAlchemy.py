from sqlalchemy import ForeignKey, Column, Boolean, DateTime
from fastapi_utils.guid_type import GUID

from src.common.infrastructure.BaseAlchemyModel import Base


__all__ = ['EventsAlchemy']


class EventsAlchemy(Base):
    __tablename__ = 'events'
    id = Column(GUID, primary_key=True)
    user_id = Column(GUID, ForeignKey('users.guid', name='fk_events__user_id'))  #? ondelete onupdate CASCADE?
    in_shift = Column(Boolean, nullable=False)
    is_work = Column(Boolean, nullable=False)
    starts_at = Column(DateTime(timezone=True), nullable=False)
    ends_at = Column(DateTime(timezone=True), nullable=False)
