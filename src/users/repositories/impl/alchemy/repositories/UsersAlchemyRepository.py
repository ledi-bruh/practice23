from uuid import UUID
from sqlalchemy.orm import Session
from src.users.repositories.core import UsersRepository, UserNotFoundException
from src.users.repositories.impl.alchemy.mappers import UsersAlchemyMapper
from src.users.repositories.impl.alchemy.models import UsersAlchemy
from src.users.services.User import User


__all__ = ['UsersAlchemyRepository']


class UsersAlchemyRepository(UsersRepository):

    __slots__ = ('__session', )

    def __init__(self, session: Session) -> None:
        self.__session = session

    def get_by_guid(self, guid: UUID) -> User:
        """Получить пользователя по guid"""

        user = (
            self.__session
            .query(UsersAlchemy)
            .filter_by(guid=guid)
            .first()
        )

        if user is None:
            raise UserNotFoundException()

        return UsersAlchemyMapper.to_domain(user)

    def create(self, user: User) -> None:
        """Создание пользователя"""

        self.__session.add(UsersAlchemyMapper.to_entity(user))

    def update(self, guid: UUID, user: User) -> None:
        """Изменить пользователя"""

        user = UsersAlchemyMapper.to_entity(self.get_by_guid(guid))

        for field, value in user:
            setattr(user, field, value)

    def delete_by_guid(self, guid: UUID) -> None:
        """Удалить пользователя по guid"""

        user = UsersAlchemyMapper.to_entity(self.get_by_guid(guid))
        self.__session.delete(user)
