from typing import Optional
from django.db.models import QuerySet

from ..models import AccountServerAccessLevel, AccountServiceAccessLevel, AccessLevel
from ..serializers.server_serializers import ServerDataSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class AccountServerAccessLevelService:
    """Класс, содержащий CRUD операции AccountServerAccessLevel model"""

    @staticmethod
    def create_account_sal(_account: User, _server: int, _access_level: int) -> None:
        acc_access_lvl = AccountServerAccessLevel.objects.create(
            account=_account,
            server_id=_server,
            access_level_id=_access_level
        )
        acc_access_lvl.save()

    @staticmethod
    def get_account_sal(_account: User, _server: int) -> Optional[AccountServerAccessLevel]:
        acc_serv_access_lvl = AccountServerAccessLevel.objects.filter(account=_account, server_id=_server).first()
        return acc_serv_access_lvl

    @staticmethod
    def get_account_sal_by_account(_account: User) -> QuerySet:
        acc_serv_access_lvl = AccountServerAccessLevel.objects.filter(account=_account).all()
        return acc_serv_access_lvl

    @staticmethod
    def get_account_sal_by_server(_server: int) -> QuerySet:
        acc_serv_access_lvl = AccountServerAccessLevel.objects.filter(server_id=_server).all()
        return acc_serv_access_lvl

    @staticmethod
    def get_account_sal_by_access_level(_access_level: str) -> QuerySet:
        level = AccessLevel.objects.filter(name=_access_level).first()
        acc_serv_access_lvl = AccountServerAccessLevel.objects.filter(access_level=level).all()
        return acc_serv_access_lvl

    @staticmethod
    def get_account_sal_by_access_level_and_user(_access_level: str, _account: User) -> QuerySet:
        level = AccessLevel.objects.filter(name=_access_level).first()
        acc_serv_access_lvl = AccountServerAccessLevel.objects.filter(access_level=level, account=_account).all()
        return acc_serv_access_lvl

    @staticmethod
    def get_account_sal_by_id(_id: int) -> Optional[AccountServerAccessLevel]:
        acc_serv_access_lvl = AccountServerAccessLevel.objects.filter(id=_id).first()
        return acc_serv_access_lvl

    @staticmethod
    def delete_account_sal_by_id(_id: int) -> None:
        AccountServerAccessLevel.objects.filter(id=_id).first().delete()


class AccountServiceAccessLevelService:
    """Класс, содержащий CRUD операции AccountServiceAccessLevel model"""

    @staticmethod
    def create_account_sal(_account: User, _access_level: int) -> None:
        acc_serv_access_lvl = AccountServiceAccessLevel.objects.create(
            account=_account,
            service_access_level_id=_access_level
        )
        acc_serv_access_lvl.save()

    @staticmethod
    def get_account_sal_by_account(_account: User) -> Optional[AccountServiceAccessLevel]:
        acc_serv_access_lvl = AccountServiceAccessLevel.objects.filter(account=_account).first()
        return acc_serv_access_lvl

    @staticmethod
    def get_account_sal_by_access_level(_access_level: int) -> Optional[AccountServiceAccessLevel]:
        acc_serv_access_lvl = AccountServiceAccessLevel.objects.filter(access_level_id=_access_level).first()
        return acc_serv_access_lvl

    @staticmethod
    def get_account_sal_by_id(_id: int) -> Optional[AccountServiceAccessLevel]:
        acc_serv_access_lvl = AccountServiceAccessLevel.objects.filter(id=_id).first()
        return acc_serv_access_lvl

    @staticmethod
    def delete_account_sal_by_id(_id: int) -> None:
        AccountServiceAccessLevel.objects.filter(id=_id).first().delete()
