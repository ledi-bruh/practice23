from uuid import UUID
from functools import partial

from src.users.domain import User
from ..models import UsersAlchemy
from ..mappers import user_db_to_domain, user_domain_to_db, event_domain_to_db
from ..AlchemyConnection import AlchemyConnection
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

    def get_by_id(self, id: UUID) -> User:
        db_user = (
            self.__session
            .query(UsersAlchemy)
            .filter_by(id=id)
            .first()
        )

        if db_user is None:
            raise UserNotFoundException()

        return user_db_to_domain(db_user)

    def create(self, user: User) -> None:
        self.__session.add(user_domain_to_db(user))

    def update(self, id: UUID, user_to_update: User) -> None:
        user = self.get_by_id(id)
        db_user = user_domain_to_db(user)

        db_user.firstname = user_to_update.name.firstname
        db_user.middlename = user_to_update.name.middlename
        db_user.lastname = user_to_update.name.lastname

        intersections = set(user.events) & set(user_to_update.events)
        events_to_delete = set(user.events) - intersections
        events_to_add = set(user_to_update.events) - intersections

        convert = partial(event_domain_to_db, user_id=id)

        new_events = set(db_user.events) - set(map(convert, events_to_delete)) + set(map(convert, events_to_add))
        db_user.events[:] = list(new_events)

    def delete_by_id(self, id: UUID) -> None:
        db_user = user_domain_to_db(self.get_by_id(id))
        self.__session.delete(db_user)
