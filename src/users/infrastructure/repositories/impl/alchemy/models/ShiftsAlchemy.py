from sqlalchemy import ForeignKey, Column, DateTime, Interval
from sqlalchemy.orm import relationship
from fastapi_utils.guid_type import GUID

from src.common.infrastructure.BaseAlchemyModel import Base


__all__ = ['ShiftsAlchemy']


class ShiftsAlchemy(Base):
    __tablename__ = 'shifts'
    id = Column(GUID, primary_key=True)
    user_id = Column(GUID, ForeignKey('users.id', name='fk_shifts__user_id', ondelete='CASCADE', onupdate='CASCADE'))
    starts_at = Column(DateTime(timezone=True), nullable=False)
    ends_at = Column(DateTime(timezone=True), nullable=False)
    work_time = Column(Interval, nullable=False)
    events = relationship('EventsAlchemy', cascade='all, delete-orphan')
