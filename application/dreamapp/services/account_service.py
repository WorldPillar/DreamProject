from typing import Optional

from django.contrib.auth import get_user_model

User = get_user_model()


class AccountService:
    """Класс, содержащий CRUD операции Account model"""

    @staticmethod
    def create_account(_username: str, _email: str, _password: str):
        user = User.objects.create(
            username=_username,
            email=_email,
            password=_password
        )
        user.save()

    @staticmethod
    def get_account_by_id(_id: int) -> Optional[User]:
        user = User.objects.filter(id=_id).first()
        return user

    @staticmethod
    def get_account_by_username(_username: str) -> Optional[User]:
        user = User.objects.filter(username=_username).first()
        return user

    @staticmethod
    def delete_account_by_id(_id: int) -> None:
        User.objects.filter(id=_id).first().delete()
