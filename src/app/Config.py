import typing as t
from pydantic import BaseModel
from pathlib import Path
from yaml import safe_load


__all__ = ['Config', 'read_config']


class Config(BaseModel):

    app: t.Mapping[str, t.Any]
    repository: t.Mapping[str, t.Any]


def read_config(path: str) -> t.Mapping:
    file_extension = Path(path).suffix

    with open(path, 'r') as config_file:

        if file_extension == '.yml':
            return safe_load(config_file)

        raise Exception(f'Configuration file with the {file_extension} extension is not supported.')
