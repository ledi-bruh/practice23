from src.users.services import Users
from src.users.repositories.impl.alchemy.models import UsersAlchemy


__all__ = ['UsersAlchemyMapper']


class UsersAlchemyMapper:

    @staticmethod
    async def to_entity(self, domain: Users) -> UsersAlchemy:
        ...

    @staticmethod
    async def to_domain(self, entity: UsersAlchemy) -> Users:
        ...
