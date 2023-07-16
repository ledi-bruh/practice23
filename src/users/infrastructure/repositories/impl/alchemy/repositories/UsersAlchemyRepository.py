from uuid import UUID
from functools import partial

from src.users.domain import User
from ..models import UsersAlchemy
from ..AlchemyConnection import AlchemyConnection
from ..mappers import user_db_to_domain, user_domain_to_db, event_domain_to_db
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
        #! Если для удобства использовать self.get_by_id(id), то там возвращается не db а domain model 
        #! => при конверте обратно в db это уже другая модель

        # user = self.get_by_id(id)

        db_user: UsersAlchemy = self.__session.query(UsersAlchemy).filter_by(id=id).one()

        db_user.firstname = user_to_update.name.firstname
        db_user.middlename = user_to_update.name.middlename
        db_user.lastname = user_to_update.name.lastname

        convert = partial(event_domain_to_db, user_id=id)
        db_user.events[:] = list(map(convert, user_to_update.events))

        # intersections = set(user.events) & set(user_to_update.events)
        # events_to_delete = set(user.events) - intersections
        # events_to_add = set(user_to_update.events) - intersections
        # new_events = set(db_user.events) - set(map(convert, events_to_delete)) | set(map(convert, events_to_add))
        # db_user.events[:] = list(new_events)

    async def delete_by_id(self, id: UUID) -> None:
        #! как и выше, повторять get либо get должен вернуть db model
        self.__session.query(UsersAlchemy).filter_by(id=id).delete()
