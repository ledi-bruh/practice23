from uuid import UUID
from sqlalchemy.orm import Session

from src.users.domain import User
from ..models import UsersAlchemy
from ..mappers import user_db_to_domain, user_domain_to_db
from ....core import UsersRepository, UserNotFoundException


__all__ = [
    'UsersAlchemyRepository',
]


class UsersAlchemyRepository(UsersRepository):

    __slots__ = ('__session', )

    def __init__(self, session: Session) -> None:
        self.__session = session

    def get_by_id(self, id: UUID) -> User:
        """Получить пользователя по id"""

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
        """Создание пользователя"""

        self.__session.add(user_domain_to_db(user))

    def update(self, id: UUID, user: User) -> None:  #? Должен изменить юзера и в БД, и в Domain?
        """Изменить пользователя"""

        db_user = user_domain_to_db(self.get_by_id(id))

        #? Как заменять user.name и подобные?
        #? user_domain_to_db(user), не появятся какие-то ненужные поля?
        for field, value in user_domain_to_db(user).__dict__.items():
            setattr(db_user, field, value)

    def delete_by_id(self, id: UUID) -> None:
        """Удалить пользователя по id"""

        db_user = user_domain_to_db(self.get_by_id(id))
        self.__session.delete(db_user)
