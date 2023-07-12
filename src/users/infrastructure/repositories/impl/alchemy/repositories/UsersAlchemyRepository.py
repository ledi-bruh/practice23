from uuid import UUID
from functools import partial
from sqlalchemy.orm import Session

from src.users.domain import User
from ..models import UsersAlchemy
from ..mappers import user_db_to_domain, user_domain_to_db, event_domain_to_db
from ....core import UsersRepository, UserNotFoundException


__all__ = ['UsersAlchemyRepository']


class UsersAlchemyRepository(UsersRepository):

    __slots__ = ('__session', )

    def __init__(self, session: Session) -> None:
        self.__session = session

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

    def update(self, id: UUID, user_to_update: User) -> None:  #! Нужен ли тогда id, если он есть в User?
        db_user = user_domain_to_db(self.get_by_id(id))

        db_user.firstname = user_to_update.name.firstname
        db_user.middlename = user_to_update.name.middlename
        db_user.lastname = user_to_update.name.lastname

        db_user.events[:] = list(map(partial(event_domain_to_db, user_id=db_user.id), user_to_update.events))

    def delete_by_id(self, id: UUID) -> None:
        db_user = user_domain_to_db(self.get_by_id(id))
        self.__session.delete(db_user)
