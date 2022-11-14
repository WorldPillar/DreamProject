from typing import Optional

from ..models import AccessLevel, ServiceAccessLevel


class AccessLevelService:
    """Класс, содержащий CRUD операции AccessLevel model"""

    @staticmethod
    def create_access_level(_level: int, _name: str) -> None:
        access_level = AccessLevel.objects.create(
            name=_name
        )
        access_level.save()

    @staticmethod
    def get_access_level_by_id(_id: int) -> Optional[AccessLevel]:
        level = AccessLevel.objects.filter(id=_id).first()
        return level

    @staticmethod
    def get_access_level_by_name(_name: str) -> Optional[AccessLevel]:
        level = AccessLevel.objects.filter(name=_name).first()
        return level

    @staticmethod
    def update_access_level_name(_id: int, _name: str) -> None:
        AccessLevel.objects.filter(id=_id).update(name=_name)

    @staticmethod
    def delete_access_level_by_id(_id: int) -> None:
        AccessLevel.objects.filter(id=_id).delete()


class ServiceAccessLevelService:
    """Класс, содержащий CRUD операции ServiceAccessLevel model"""

    @staticmethod
    def create_service_access_level(_level: int, _name: str) -> None:
        access_level = ServiceAccessLevel.objects.create(
            name=_name
        )
        access_level.save()

    @staticmethod
    def get_service_access_level_by_id(_id: int) -> Optional[ServiceAccessLevel]:
        level = ServiceAccessLevel.objects.filter(id=_id).first()
        return level

    @staticmethod
    def get_service_access_level_by_name(_name: str) -> Optional[ServiceAccessLevel]:
        level = ServiceAccessLevel.objects.filter(name=_name).first()
        return level

    @staticmethod
    def update_service_access_level_name(_id: int, _name: str) -> None:
        ServiceAccessLevel.objects.filter(id=_id).update(name=_name)

    @staticmethod
    def delete_service_access_level_by_id(_id: int) -> None:
        ServiceAccessLevel.objects.filter(id=_id).delete()