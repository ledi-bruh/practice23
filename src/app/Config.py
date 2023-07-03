import typing as t
from pydantic import BaseModel
from yaml import safe_load


__all__ = ['Config', 'config']


class Config(BaseModel):

    app: t.Optional[t.Mapping[str, t.Any]]
    repository: t.Optional[t.Mapping[str, t.Any]]

    def load(self, path: str) -> None:
        with open(path, 'r') as f:
            self.__dict__.update(safe_load(f))


config = Config()
config.load('config.yaml')
