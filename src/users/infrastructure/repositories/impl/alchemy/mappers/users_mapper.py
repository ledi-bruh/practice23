from src.users.domain import User, Name
from ..models import UsersAlchemy


__all__ = [
    'user_domain_to_db',
    'user_db_to_domain',
]


def user_domain_to_db(user: User) -> UsersAlchemy:
    return UsersAlchemy(
        id=user._id,
        firstname=user._name._firstname,
        middlename=user._name._middlename,
        lastname=user._name._lastname,
    )


def user_db_to_domain(db_user: UsersAlchemy) -> User:
    user = User.__new__(User)
    user.__dict__.update({'_' + k: v for k, v in db_user.__dict__.items()})
    user._name = Name(
        firstname=db_user.firstname,
        middlename=db_user.middlename,
        lastname=db_user.lastname,
    )
    user._events_map = {e._id: e for e in user._events}
    return user
