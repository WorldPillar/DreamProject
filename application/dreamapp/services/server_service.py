from typing import Optional

from rest_framework.request import Request
from typing import Optional
from django.db.models import QuerySet

from ..models import ServerData
from ..serializers.server_serializers import ServerDataSerializer, UpdateServerDataSerializer


class ServerDataService:
    """Класс, содержащий CRUD операции ServerData model"""

    # @staticmethod
    # def create_server_data(_ip: str, _port: int, _name: str) -> None:
    #     server = ServerData.objects.create(
    #         ip=_ip,
    #         port=_port,
    #         name=_name
    #     )
    #     server.save()

    @staticmethod
    def create_server_data(request: Request) -> bool:
        serializer = ServerDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(f'Server was created')
            return True
        print(f'Error in creating')
        return False

    @staticmethod
    def get_server_by_id(_id: int) -> Optional[ServerData]:
        server = ServerData.objects.filter(id=_id).first()
        return server

    @staticmethod
    def get_server_by_name(_name: str) -> Optional[ServerData]:
        server = ServerData.objects.filter(name=_name).first()
        return server

    @staticmethod
    def get_server_by_permission() -> ServerDataSerializer:
        server = ServerData.objects.all()
        serializer = ServerDataSerializer(server, many=True)
        return serializer

    @staticmethod
    def update_server_data(_id: int, request: Request) -> bool:
        instance = ServerData.objects.filter(id=_id).first()
        serializer = UpdateServerDataSerializer(data=request.data, instance=instance)
        if serializer.is_valid():
            serializer.save()
            return True
        return False

    @staticmethod
    def delete_server_data_by_id(_id: int) -> bool:
        server = ServerData.objects.filter(id=_id).first()
        if server is not None:
            server.delete()
            return True
        return False
