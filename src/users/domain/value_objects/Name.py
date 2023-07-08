
__all__ = ['Name']


class Name:

    __slots__ = (
        '_firstname',
        '_middlename',
        '_lastname',
    )

    def __init__(self, firstname: str, middlename: str, lastname: str) -> None:
        self._firstname = firstname
        self._middlename = middlename
        self._lastname = lastname

    @property
    def firstname(self):
        return self._firstname

    @property
    def middlename(self):
        return self._middlename

    @property
    def lastname(self):
        return self._lastname
