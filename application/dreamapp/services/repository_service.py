from typing import Optional
from django.db.models import QuerySet

from ..models import Account, ServerData, AccessLevel, FriendList,\
    NewsData, AccountAccessLevel, ServerAccessLevel


class AccountService:
    """Класс, содержащий CRUD операции Account model"""

    @staticmethod
    def create_account(_username: str, _email: str, _password: str):
        account = Account.objects.create(
            username=_username,
            email=_email,
            password=_password
        )
        account.save()

    @staticmethod
    def get_account_by_id(_id: int) -> Optional[Account]:
        account = Account.objects.filter(id=_id).first()
        return account

    @staticmethod
    def get_account_by_username(_username: str) -> Optional[Account]:
        account = Account.objects.filter(username=_username).first()
        return account

    @staticmethod
    def delete_account_by_id(_id: int) -> None:
        Account.objects.filter(id=_id).first().delete()


class ServerDataService:
    """Класс, содержащий CRUD операции ServerData model"""

    @staticmethod
    def create_server_data(_ip: str, _port: int, _name: str) -> None:
        server = ServerData.objects.create(
            ip=_ip,
            port=_port,
            name=_name
        )
        server.save()

    @staticmethod
    def get_server_by_id(_id: int) -> Optional[ServerData]:
        server = ServerData.objects.filter(id=_id).first()
        return server

    @staticmethod
    def get_server_by_name(_name: str) -> Optional[ServerData]:
        server = ServerData.objects.filter(name=_name).first()
        return server

    @staticmethod
    def update_server_data_ip_and_port(_id: int, _ip: str, _port: int) -> None:
        ServerData.objects.filter(id=_id).update(ip=_ip, port=_port)

    @staticmethod
    def delete_server_data_by_id(_id: int) -> None:
        ServerData.objects.filter(id=_id).first().delete()


class AccessLevelService:
    """Класс, содержащий CRUD операции AccessLevel model"""

    @staticmethod
    def create_access_level(_level: int, _name: str) -> None:
        access_level = AccessLevel.objects.create(
            level=_level,
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


class FriendListService:
    """Класс, содержащий CRUD операции FriendList model"""

    @staticmethod
    def create_friend_list(_owner: int, _friend: int) -> None:
        friend_list = FriendList.objects.create(
            owner_id=_owner,
            friend_id=_friend
        )
        friend_list.save()

    @staticmethod
    def get_friend_list_by_owner(_owner: int) -> QuerySet:
        friend_list = FriendList.objects.filter(owner_id=_owner).all()
        return friend_list

    @staticmethod
    def get_friend_list_by_friend(_friend: int) -> QuerySet:
        friend_list = FriendList.objects.filter(friend_id=_friend).all()
        return friend_list

    @staticmethod
    def get_friend_list_by_id(_id: int) -> Optional[FriendList]:
        friend_list = FriendList.objects.filter(id=_id).first()
        return friend_list

    @staticmethod
    def delete_friend_list_by_id(_id: int) -> None:
        FriendList.objects.filter(id=_id).delete()


class NewsDataService:
    """Класс, содержащий CRUD операции NewsData model"""

    @staticmethod
    def create_news_data(_author: int, _topic: str, _text: str) -> None:
        news_data = NewsData.objects.create(
            author_id=_author,
            topic=_topic,
            text=_text
        )
        news_data.save()

    @staticmethod
    def get_news_data_by_id(_id: int) -> Optional[NewsData]:
        news_data = NewsData.objects.filter(id=_id).first()
        return news_data

    @staticmethod
    def get_news_data_by_author(_author: int) -> QuerySet:
        news_data = NewsData.objects.filter(author_id=_author).all()
        return news_data

    @staticmethod
    def delete_news_data_by_id(_id: int) -> None:
        NewsData.objects.filter(id=_id).first().delete()


class AccountAccessLevelService:
    """Класс, содержащий CRUD операции AccountAccessLevel model"""

    @staticmethod
    def create_account_access_level(_account: int, _access_level: int) -> None:
        acc_access_lvl = AccountAccessLevel.objects.create(
            account_id=_account,
            access_level_id=_access_level
        )
        acc_access_lvl.save()

    @staticmethod
    def get_account_access_level_by_account(_account: int) -> QuerySet:
        acc_access_lvl = AccountAccessLevel.objects.filter(account_id=_account).all()
        return acc_access_lvl

    @staticmethod
    def get_account_access_level_by_access_level(_access_level: int) -> QuerySet:
        acc_access_lvl = AccountAccessLevel.objects.filter(access_level_id=_access_level).all()
        return acc_access_lvl

    @staticmethod
    def get_account_access_level_by_id(_id: int) -> Optional[AccountAccessLevel]:
        acc_access_lvl = AccountAccessLevel.objects.filter(id=_id).first()
        return acc_access_lvl

    @staticmethod
    def delete_account_access_level_by_id(_id: int) -> None:
        AccountAccessLevel.objects.filter(id=_id).first().delete()


class ServerAccessLevelService:
    """Класс, содержащий CRUD операции ServerAccessLevel model"""

    @staticmethod
    def create_server_access_level(_server: int, _access_level: int) -> None:
        serv_access_lvl = ServerAccessLevel.objects.create(
            server_id=_server,
            access_level_id=_access_level
        )
        serv_access_lvl.save()

    @staticmethod
    def get_server_access_level_by_server(_server: int) -> QuerySet:
        serv_access_lvl = ServerAccessLevel.objects.filter(server_id=_server).all()
        return serv_access_lvl

    @staticmethod
    def get_server_access_level_by_access_level(_access_level: int) -> QuerySet:
        serv_access_lvl = ServerAccessLevel.objects.filter(access_level_id=_access_level).all()
        return serv_access_lvl

    @staticmethod
    def get_server_access_level_by_id(_id: int) -> Optional[ServerAccessLevel]:
        serv_access_lvl = ServerAccessLevel.objects.filter(id=_id).first()
        return serv_access_lvl

    @staticmethod
    def delete_server_access_level_by_id(_id: int) -> None:
        ServerAccessLevel.objects.filter(id=_id).first().delete()
