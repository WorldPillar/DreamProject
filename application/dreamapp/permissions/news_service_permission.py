from ..services.account_access_service import AccountServiceAccessLevelService


class NewsPermission:

    @staticmethod
    def publish_permission(user) -> bool:
        try:
            if AccountServiceAccessLevelService.get_account_sal_by_account(user).access_level.name == "first":
                print(f'Admission allowed')
                return True
        except PermissionError:
            print(f'Admission denied')
        return False


    @staticmethod
    def delete_permission(user) -> bool:
        try:
            if AccountServiceAccessLevelService.get_account_sal_by_account(user).access_level.name == "first":
                print(f'Admission allowed')
                return True
        except PermissionError:
            print(f'Admission denied')
        return False
