from src.users.services import User
from src.users.repositories.impl.alchemy.models import UsersAlchemy


__all__ = ['UsersAlchemyMapper']


class UsersAlchemyMapper:

    __slots__ = ()

    @staticmethod
    async def to_entity(domain: User) -> UsersAlchemy:
        return UsersAlchemy(**dict(domain))

    @staticmethod
    async def to_domain(entity: UsersAlchemy) -> User:
        return User(**entity.__dict__)
