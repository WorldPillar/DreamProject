from django.test import TestCase
import random
from .services.repository_service import *

# Create your tests here.


class FriendListTestCase(TestCase):
    def setUp(self):
        AccountService.create_account(_username='first', _email='first', _password='0')
        AccountService.create_account(_username='second', _email='second', _password='0')
        owner = AccountService.get_account_by_username('first').id
        friend = AccountService.get_account_by_username('second').id
        FriendListService.create_friend_list(_owner=owner, _friend=friend)

    def test_get_friend_list_by_owner(self):
        owner = AccountService.get_account_by_username('first').id
        friend_list_rows = FriendListService.get_friend_list_by_owner(_owner=owner)
        for row in friend_list_rows:
            print(row)
            self.assertIsNotNone(row)
            self.assertTrue(row.owner.username == 'first')
            self.assertTrue(row.friend.username == 'second')

    def test_get_friend_list_by_friend(self):
        friend = AccountService.get_account_by_username('second').id
        friend_list_rows = FriendListService.get_friend_list_by_friend(_friend=friend)
        for row in friend_list_rows:
            print(row)
            self.assertIsNotNone(row)
            self.assertTrue(row.owner.username == 'first')
            self.assertTrue(row.friend.username == 'second')

    def test_get_friend_list_by_id(self):
        friends = FriendListService.get_friend_list_by_id(_id=3)
        print(friends)
        self.assertIsNotNone(friends)
        self.assertTrue(friends.owner.username == 'first')
        self.assertTrue(friends.friend.username == 'second')

    def test_delete_friend_list_by_id(self):
        FriendListService.delete_friend_list_by_id(_id=4)
        result = FriendListService.get_friend_list_by_id(_id=4)
        self.assertIsNone(result)

    def tearDown(self):
        pass


class NewsDataTestCase(TestCase):
    def setUp(self):
        AccountService.create_account(_username='first', _email='first', _password='0')
        author = AccountService.get_account_by_username('first').id
        NewsDataService.create_news_data(_author=author, _topic="Hello", _text="Hi")

    def test_get_news_data_by_author(self):
        author = AccountService.get_account_by_username('first').id
        news = NewsDataService.get_news_data_by_author(_author=author)
        for row in news:
            print(row)
            self.assertIsNotNone(row)
            self.assertTrue(row.author.username == 'first')

    def test_get_news_data_by_id(self):
        news = NewsDataService.get_news_data_by_id(_id=3)
        print(news)
        self.assertIsNotNone(news)
        self.assertTrue(news.author.username == 'first')

    def test_delete_news_data_by_id(self):
        NewsDataService.delete_news_data_by_id(_id=1)
        result = NewsDataService.get_news_data_by_id(_id=1)
        self.assertIsNone(result)

    def tearDown(self):
        pass


class AccountAccessLevelTestCase(TestCase):
    def setUp(self):
        AccountService.create_account(_username='first', _email='first', _password='0')
        account = AccountService.get_account_by_username('first').id
        AccessLevelService.create_access_level(_level=1, _name='zero')
        access = AccessLevelService.get_access_level_by_name(_name='zero').id
        AccountAccessLevelService.create_account_access_level(_account=account, _access_level=access)

    def test_get_account_access_level_by_account(self):
        account = AccountService.get_account_by_username('first').id
        result = AccountAccessLevelService.get_account_access_level_by_account(_account=account)
        for row in result:
            print(row)
            self.assertIsNotNone(row)
            self.assertTrue(row.account.username == 'first')
            self.assertTrue(row.access_level.name == 'zero')

    def test_get_account_access_level_by_access_level(self):
        access = AccessLevelService.get_access_level_by_name('zero').id
        result = AccountAccessLevelService.get_account_access_level_by_access_level(_access_level=access)
        for row in result:
            print(row)
            self.assertIsNotNone(row)
            self.assertTrue(row.account.username == 'first')
            self.assertTrue(row.access_level.name == 'zero')

    def test_get_account_access_level_by_id(self):
        result = AccountAccessLevelService.get_account_access_level_by_id(_id=4)
        print(result)
        self.assertIsNotNone(result)
        self.assertTrue(result.account.username == 'first')
        self.assertTrue(result.access_level.name == 'zero')

    def test_delete_account_access_level_by_id(self):
        AccountAccessLevelService.delete_account_access_level_by_id(_id=1)
        result = AccountAccessLevelService.get_account_access_level_by_id(_id=1)
        self.assertIsNone(result)

    def tearDown(self):
        pass


class ServerAccessLevelTestCase(TestCase):
    def setUp(self):
        ServerDataService.create_server_data(_name='first', _ip='first', _port=0)
        server = ServerDataService.get_server_by_name('first').id
        AccessLevelService.create_access_level(_level=1, _name='zero')
        access = AccessLevelService.get_access_level_by_name(_name='zero').id
        ServerAccessLevelService.create_server_access_level(_server=server, _access_level=access)

    def test_get_server_access_level_by_server(self):
        server = ServerDataService.get_server_by_name('first').id
        result = ServerAccessLevelService.get_server_access_level_by_server(_server=server)
        for row in result:
            print(row)
            self.assertIsNotNone(row)
            self.assertTrue(row.server.name == 'first')
            self.assertTrue(row.access_level.name == 'zero')

    def test_get_server_access_level_by_access_level(self):
        access = AccessLevelService.get_access_level_by_name('zero').id
        result = ServerAccessLevelService.get_server_access_level_by_access_level(_access_level=access)
        for row in result:
            print(row)
            self.assertIsNotNone(row)
            self.assertTrue(row.server.name == 'first')
            self.assertTrue(row.access_level.name == 'zero')

    def test_get_server_access_level_by_id(self):
        result = ServerAccessLevelService.get_server_access_level_by_id(_id=3)
        print(result)
        self.assertIsNotNone(result)
        self.assertTrue(result.server.name == 'first')
        self.assertTrue(result.access_level.name == 'zero')

    def test_delete_server_access_level_by_id(self):
        ServerAccessLevelService.delete_server_access_level_by_id(_id=1)
        result = ServerAccessLevelService.get_server_access_level_by_id(_id=1)
        self.assertIsNone(result)

    def tearDown(self):
        pass


class ServerDataTestCase(TestCase):
    def setUp(self):
        ServerDataService.create_server_data(_ip='0:0', _port=0, _name='server')

    def test_update_server_data_ip_and_port(self):
        server = ServerDataService.get_server_by_name(_name='server').id
        ServerDataService.update_server_data_ip_and_port(_id=server, _ip='1:1', _port=1)
        result = ServerDataService.get_server_by_id(_id=server)
        self.assertIsNotNone(result)
        self.assertTrue(result.ip == '1:1')
        self.assertTrue(result.port == 1)

    def test_delete_server_data_by_id(self):
        server = ServerDataService.get_server_by_name(_name='server').id
        ServerDataService.delete_server_data_by_id(_id=server)
        result = ServerDataService.get_server_by_id(_id=server)
        self.assertIsNone(result)

    def tearDown(self):
        pass


class AccessLevelTestCase(TestCase):
    def setUp(self):
        AccessLevelService.create_access_level(_level=1, _name='access')

    def test_update_access_level_name(self):
        access = AccessLevelService.get_access_level_by_name(_name='access').id
        AccessLevelService.update_access_level_name(_id=access, _name='newone')
        result = AccessLevelService.get_access_level_by_id(_id=access)
        self.assertIsNotNone(result)
        self.assertTrue(result.name == 'newone')

    def test_delete_access_level_by_id(self):
        access = AccessLevelService.get_access_level_by_name(_name='access').id
        AccessLevelService.delete_access_level_by_id(_id=access)
        result = AccessLevelService.get_access_level_by_id(_id=access)
        self.assertIsNone(result)

    def tearDown(self):
        pass
