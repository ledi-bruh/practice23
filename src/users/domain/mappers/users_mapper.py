from src.users.presentation.models import UserUI
from ..entities.User import User
from .event_mapper import event_domain_to_ui


__all__ = [
    'user_domain_to_ui',
]


def user_domain_to_ui(user: User) -> UserUI:
    return UserUI(
        id=user.id,
        firstname=user.name.firstname,
        middlename=user.name.middlename,
        lastname=user.name.lastname,
        events=list(map(event_domain_to_ui, user.events)),
    )
