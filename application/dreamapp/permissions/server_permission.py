from ..services.account_access_service import AccountServiceAccessLevelService
from ..services.account_access_service import AccountServerAccessLevelService
from django.db.models import QuerySet


class ServerPermission:

    @staticmethod
    def permission(user) -> bool:
        try:
            if AccountServiceAccessLevelService.get_account_sal_by_account(user).access_level.name == "first":
                print(f'Admission allowed')
                return True
        except PermissionError:
            print(f'Admission denied')
        return False


class GetBanServers:

    @staticmethod
    def banservers(user) -> QuerySet:
        return AccountServerAccessLevelService.get_account_sal_by_access_level_and_user("Ban", user)

