from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from ..services.friend_news_service import FriendListService


class FriendListGetAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        """ Getting last n news """
        response = FriendListService.get_friend_list_by_owner(request.user)
        return Response(data=response.data, status=status.HTTP_200_OK)


class FriendListPostDeleteAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, friend: str) -> Response:
        """ Adding new server with permission """
        if FriendListService.create_friend_list(request.user, friend):
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, friend: str) -> Response:
        """ Deleting server by id """
        if FriendListService.delete_friend_list(request.user, friend):
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
