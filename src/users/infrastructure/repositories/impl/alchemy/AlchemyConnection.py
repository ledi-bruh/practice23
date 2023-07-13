import typing as t
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

from ...core import Connection


__all__ = ['AlchemyConnection']


class AlchemyConnection(Connection):

    __slots__ = (
        '__config',
        '__session',
    )

    def __init__(self, repository_config: t.Mapping[str, t.Any]) -> None:
        self.__config = repository_config
        self.__session = None

    def initialize(self):
        if self.__session is not None:
            return

        connection_string = URL.create(
            drivername=self.__config['db_driver'],
            username=self.__config['db_login'],
            password=self.__config['db_password'],
            host=self.__config['db_host'],
            port=self.__config['db_port'],
            database=self.__config['db_database']
        )

        engine = create_engine(connection_string)

        Session = sessionmaker(
            engine,
            autocommit=False,
            autoflush=False,
        )

        self.__session = Session()

    def deinitialize(self):
        if self.__session is not None:
            self.__session.close()

    def commit(self) -> None:
        self.__session.commit()

    def rollback(self) -> None:
        self.__session.rollback()
