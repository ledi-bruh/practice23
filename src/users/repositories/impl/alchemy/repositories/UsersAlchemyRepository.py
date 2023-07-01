from sqlalchemy.orm import Session
from src.users.repositories.core import UsersRepository, UserNotFoundException
from src.users.repositories.impl.alchemy.mappers import UsersAlchemyMapper
from src.users.repositories.impl.alchemy.models import UsersAlchemy
from src.users.services.Users import Users


__all__ = ['UsersAlchemyRepository']


class UsersAlchemyRepository(UsersRepository):

    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_id(self, id: int) -> Users:
        """Получить пользователя по id"""

        user = (
            self.session
            .query(UsersAlchemy)
            .filter_by(id=id)
            .first()
        )
        if user is None:
            raise UserNotFoundException()

        return UsersAlchemyMapper.to_domain(user)

    def create(self, user: Users) -> None:
        """Создание пользователя"""

        self.session.add(UsersAlchemyMapper.to_entity(user))


    def update(self, id: int, user: Users) -> None:
        """Изменить пользователя"""
        
        user = UsersAlchemyMapper.to_entity(self.get_by_id(id))
        
        for field, value in user:
            setattr(user, field, value)


    def delete_by_id(self, id: int) -> None:
        """Удалить пользователя по id"""
        
        user = UsersAlchemyMapper.to_entity(self.get_by_id(id))
        self.session.delete(user)
