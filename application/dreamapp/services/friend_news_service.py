from rest_framework.request import Request
from typing import Optional
from django.db.models import QuerySet

from ..models import FriendList, NewsData
from ..serializers.news_serializers import GetNewsDataSerializer, PostNewsDataSerializer
from ..serializers.friendlist_serializers import GetFriendListSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class FriendListService:
    """Класс, содержащий CRUD операции FriendList model"""

    # @staticmethod
    # def create_friend_list(_owner: int, _friend: int) -> None:
    #     friend_list = FriendList.objects.create(
    #         owner_id=_owner,
    #         friend_id=_friend
    #     )
    #     friend_list.save()

    @staticmethod
    def create_friend_list(_owner: User, _friend: str) -> (bool, dict):
        friend = User.objects.filter(username=_friend).first()
        friendInList = FriendList.objects.filter(owner=_owner, friend=friend).first()
        try:
            if friend is None:
                raise NameError()
            if friendInList is not None:
                raise Exception()
            friend_list = FriendList.objects.create(
                owner=_owner,
                friend=friend
            )
            friend_list.save()
            response = {"message": "Friend list was created"}
            return True, response
        except NameError:
            response = {"message": "User does not exist"}
            return False, response
        except Exception:
            response = {"message": "User is already in the friendlist"}
            return False, response

    @staticmethod
    def get_friend_list_by_owner(_owner: User) -> GetFriendListSerializer:
        friend_list = FriendList.objects.filter(owner=_owner).all()
        response = GetFriendListSerializer(friend_list, many=True)
        return response

    @staticmethod
    def get_friend_list_by_friend(_friend: User) -> QuerySet:
        friend_list = FriendList.objects.filter(friend=_friend).all()
        return friend_list

    @staticmethod
    def get_friend_list_by_id(_id: int) -> Optional[FriendList]:
        friend_list = FriendList.objects.filter(id=_id).first()
        return friend_list

    @staticmethod
    def delete_friend_list_by_id(_id: int) -> None:
        FriendList.objects.filter(id=_id).delete()

    @staticmethod
    def delete_friend_list(_owner: User, _friend: str) -> bool:
        friend = User.objects.filter(username=_friend).first()
        if friend is not None:
            FriendList.objects.filter(owner=_owner, friend=friend).delete()
            return True
        return False


class NewsDataService:
    """Класс, содержащий CRUD операции NewsData model"""

    # @staticmethod
    # def create_news_data(_author: int, _topic: str, _text: str) -> None:
    #     news_data = NewsData.objects.create(
    #         author_id=_author,
    #         topic=_topic,
    #         text=_text
    #     )
    #     news_data.save()

    @staticmethod
    def create_news_data(request: Request) -> bool:
        serializer = PostNewsDataSerializer(context={'request': request}, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(f'News was created')
            return True
        print(f'Error in creating')
        return False

    @staticmethod
    def get_news_data_by_id(_id: int) -> Optional[NewsData]:
        news_data = NewsData.objects.filter(id=_id).first()
        return news_data

    @staticmethod
    def get_news_data_by_author(_author: int) -> QuerySet:
        news_data = NewsData.objects.filter(author=_author).all()
        return news_data

    @staticmethod
    def get_last_news(count: int) -> GetNewsDataSerializer:
        news_data = NewsData.objects.order_by('-date')[:count]
        response = GetNewsDataSerializer(news_data, many=True)
        return response

    @staticmethod
    def delete_news_data_by_id(_id: int) -> bool:
        news = NewsData.objects.filter(id=_id).first()
        if news is not None:
            news.delete()
            return True
        return False
