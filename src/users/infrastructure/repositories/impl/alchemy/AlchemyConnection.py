import typing as t
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

from ...core import Connection


__all__ = ['AlchemyConnection']


class AlchemyConnection(Connection):

    __slots__ = (
        '__config',
        '_session',
    )

    def __init__(self, repository_config: t.Mapping[str, t.Any]) -> None:
        self.__config = repository_config
        self._session = None

    def initialize(self):
        if self._session is not None:
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

        self._session = Session()

    def deinitialize(self):
        if self._session is not None:
            self._session.close()

    def commit(self) -> None:
        self._session.commit()

    def rollback(self) -> None:
        self._session.rollback()
