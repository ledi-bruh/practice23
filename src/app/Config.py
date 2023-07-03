from pydantic import BaseModel
from yaml import safe_load


__all__ = ['Config', 'config']


class Config(BaseModel):

    app: dict
    repository: dict

    def __init__(self, path):
        with open(path, 'r') as f:
            self.__dict__.update(safe_load(f))


config = Config('config.yaml')
