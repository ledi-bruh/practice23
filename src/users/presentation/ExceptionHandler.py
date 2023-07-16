from fastapi import FastAPI, Request, HTTPException
from sqlalchemy.exc import NoResultFound


__all__ = ['ExceptionHandler']


class ExceptionHandler:

    def __init__(self, app: FastAPI) -> None:
        self.__app = app

    async def __no_result_found(self, request: Request, exc: NoResultFound) -> None:
        return HTTPException(status_code=500, detail='No result found')

    async def initialize(self) -> None:
        self.__app.add_exception_handler(Exception, self.__no_result_found)

    async def deinitialize(self):
        pass
