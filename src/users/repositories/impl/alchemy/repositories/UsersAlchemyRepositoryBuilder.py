import typing as t
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

from ....core import UsersRepositoryBuilder
from .UsersAlchemyRepository import UsersAlchemyRepository


__all__ = ['UsersAlchemyRepositoryBuilder']


class UsersAlchemyRepositoryBuilder(UsersRepositoryBuilder):

    __slots__ = ()

    def make_session(self, repository_config: t.Mapping):
        connection_string = URL.create(
            drivername=repository_config['db_driver'],
            username=repository_config['db_login'],
            password=repository_config['db_password'],
            host=repository_config['db_host'],
            port=repository_config['db_port'],
            database=repository_config['db_database']
        )

        engine = create_engine(connection_string)

        Session = sessionmaker(
            engine,
            autocommit=False,
            autoflush=False,
        )

        return Session()

    def __call__(self, repository_config: t.Mapping, **kwargs: t.Mapping) -> UsersAlchemyRepository:
        return UsersAlchemyRepository(self.make_session(repository_config))
