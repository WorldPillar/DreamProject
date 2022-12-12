from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework .permissions import IsAuthenticated

from ..serializers.news_serializers import PostNewsDataSerializer, GetNewsDataSerializer
from ..services.friend_news_service import NewsDataService
from ..permissions.news_service_permission import NewsPermission


class NewsGetAPIView(GenericAPIView):
    serializer_class = GetNewsDataSerializer

    def get(self, request: Request, pk: int = 3) -> Response:
        """ Getting last n news """
        response = NewsDataService.get_last_news(pk)
        return Response(data=response.data, status=status.HTTP_200_OK)


class NewsPostAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostNewsDataSerializer

    def post(self, request: Request) -> Response:
        """ Adding new news with permission """
        if NewsPermission.publish_permission(request.user):
            if NewsDataService.create_news_data(request):
                return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class NewsDeleteAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request: Request, pk: int) -> Response:
        """ Deleting news by id """
        if NewsPermission.delete_permission(request.user):
            NewsDataService.delete_news_data_by_id(pk)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
