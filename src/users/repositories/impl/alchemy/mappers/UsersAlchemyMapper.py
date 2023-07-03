from src.users.services import Users
from src.users.repositories.impl.alchemy.models import UsersAlchemy


__all__ = ['UsersAlchemyMapper']


class UsersAlchemyMapper:

    @staticmethod
    async def to_entity(domain: Users) -> UsersAlchemy:
        return UsersAlchemy(**dict(domain))

    @staticmethod
    async def to_domain(entity: UsersAlchemy) -> Users:
        return Users(**entity.__dict__)
