from uuid import UUID
from functools import partial

from src.users.domain import User
from ..models import UsersAlchemy
from ..AlchemyConnection import AlchemyConnection
from ..mappers import user_db_to_domain, user_domain_to_db, event_domain_to_db, shift_domain_to_db
from ....core import UsersRepository, UserNotFoundException


__all__ = ['UsersAlchemyRepository']


class UsersAlchemyRepository(UsersRepository):

    __slots__ = (
        '__connection',
    )

    def __init__(self, connection: AlchemyConnection) -> None:
        self.__connection = connection

    @property
    def __session(self):
        return self.__connection.session

    async def get_by_id(self, id: UUID) -> User:
        db_user = (
            self.__session
            .query(UsersAlchemy)
            .filter_by(id=id)
            .one()
        )

        return user_db_to_domain(db_user)

    async def create(self, user: User) -> None:
        self.__session.add(user_domain_to_db(user))

    async def update(self, id: UUID, user_to_update: User) -> None:
        db_user: UsersAlchemy = self.__session.query(UsersAlchemy).filter_by(id=id).one()

        db_user.firstname = user_to_update.name.firstname
        db_user.middlename = user_to_update.name.middlename
        db_user.lastname = user_to_update.name.lastname

        events_to_add = []
        events = set(user_to_update.events)

        for shift in user_to_update.shifts:
            shift_events = set(shift.events)
            events_to_add += list(map(partial(event_domain_to_db, user_id=id, shift_id=shift.id), shift_events))
            events -= shift_events

        events_to_add += list(map(partial(event_domain_to_db, user_id=id, shift_id=None), events))
        db_user.events[:] = events_to_add

        db_user.shifts[:] = list(map(partial(shift_domain_to_db, user_id=id), user_to_update.shifts))

    async def delete_by_id(self, id: UUID) -> None:
        self.__session.query(UsersAlchemy).filter_by(id=id).delete()
