from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from ..serializers.server_serializers import ServerDataSerializer, UpdateServerDataSerializer
from ..services.server_service import ServerDataService
from ..permissions.server_permission import ServerPermission


class ServerDataGetAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        """ Getting last n news """
        response = ServerDataService.get_server_by_permission()
        return Response(data=response.data, status=status.HTTP_200_OK)


class ServerDataPostAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ServerDataSerializer

    def post(self, request: Request) -> Response:
        """ Adding new server with permission """
        if ServerPermission.permission(request.user):
            if ServerDataService.create_server_data(request):
                return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ServerDataUpdateAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateServerDataSerializer

    def put(self, request: Request, pk: int) -> Response:
        """ Updating server by id """
        if ServerPermission.permission(request.user):
            if ServerDataService.update_server_data(pk, request):
                return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ServerDataDeleteAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request: Request, pk: int) -> Response:
        """ Deleting server by id """
        if ServerPermission.permission(request.user):
            if ServerDataService.delete_server_data_by_id(pk):
                return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
