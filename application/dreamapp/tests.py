from django.test import TransactionTestCase
from .services.friend_news_service import NewsDataService, FriendListService
from .services.access_service import AccessLevelService, ServiceAccessLevelService
from .services.account_service import AccountService
from .services.server_service import ServerDataService
from .services.account_access_service import AccountServiceAccessLevelService, AccountServerAccessLevelService


class FriendListTestCase(TransactionTestCase):
    reset_sequences = True  # Сбрасываем последовательность перед запуском тестов

    def setUp(self):
        AccountService.create_account(_username='first', _email='first', _password='0')
        AccountService.create_account(_username='second', _email='second', _password='0')
        FriendListService.create_friend_list(_owner=1, _friend=2)

    def test_get_friend_list_by_owner(self):
        """ Тест функции поиска записи FriendList по владельцу """
        friend_list_rows = FriendListService.get_friend_list_by_owner(_owner=1)
        for row in friend_list_rows:
            print(row)
            self.assertIsNotNone(row)
            self.assertTrue(row.owner.username == 'first')
            self.assertTrue(row.friend.username == 'second')

    def test_get_friend_list_by_friend(self):
        """ Тест функции поиска записи FriendList по другу """
        friend_list_rows = FriendListService.get_friend_list_by_friend(_friend=2)
        for row in friend_list_rows:
            print(row)
            self.assertIsNotNone(row)
            self.assertTrue(row.owner.username == 'first')
            self.assertTrue(row.friend.username == 'second')

    def test_get_friend_list_by_id(self):
        """ Тест функции поиска записи FriendList по id """
        friends = FriendListService.get_friend_list_by_id(_id=1)
        print(friends)
        self.assertIsNotNone(friends)
        self.assertTrue(friends.owner.username == 'first')
        self.assertTrue(friends.friend.username == 'second')

    def test_delete_friend_list_by_id(self):
        """ Тест функции удаления записи FriendList по id """
        FriendListService.delete_friend_list_by_id(_id=1)
        result = FriendListService.get_friend_list_by_id(_id=1)
        self.assertIsNone(result)

    def tearDown(self):
        pass


class NewsDataTestCase(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        AccountService.create_account(_username='first', _email='first', _password='0')
        NewsDataService.create_news_data(_author=1, _topic="Hello", _text="Hi")

    def test_get_news_data_by_author(self):
        """ Тест функции поиска записи NewsData по автору """
        news = NewsDataService.get_news_data_by_author(_author=1)
        for row in news:
            print(row)
            self.assertIsNotNone(row)
            self.assertTrue(row.author.username == 'first')

    def test_get_news_data_by_id(self):
        """ Тест функции поиска записи NewsData по id """
        news = NewsDataService.get_news_data_by_id(_id=1)
        print(news)
        self.assertIsNotNone(news)
        self.assertTrue(news.author.username == 'first')

    def test_delete_news_data_by_id(self):
        """ Тест функции удаления записи NewsData по id """
        NewsDataService.delete_news_data_by_id(_id=1)
        result = NewsDataService.get_news_data_by_id(_id=1)
        self.assertIsNone(result)

    def tearDown(self):
        pass


class ServerDataTestCase(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        ServerDataService.create_server_data(_ip='0:0', _port=0, _name='server')

    def test_update_server_data_ip_and_port(self):
        """ Тест функции обновления полей ip и port записи AccessLevel по id """
        ServerDataService.update_server_data_ip_and_port(_id=1, _ip='1:1', _port=1)
        result = ServerDataService.get_server_by_id(_id=1)
        self.assertIsNotNone(result)
        self.assertTrue(result.ip == '1:1')
        self.assertTrue(result.port == 1)

    def test_delete_server_data_by_id(self):
        """ Тест функции удаления записи AccessLevel по id """
        ServerDataService.delete_server_data_by_id(_id=1)
        result = ServerDataService.get_server_by_id(_id=1)
        self.assertIsNone(result)

    def tearDown(self):
        pass


class AccessLevelTestCase(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        AccessLevelService.create_access_level(_level=1, _name='access')

    def test_update_access_level_name(self):
        """ Тест функции обновления поля названия записи AccessLevel по id """
        AccessLevelService.update_access_level_name(_id=1, _name='newone')
        result = AccessLevelService.get_access_level_by_id(_id=1)
        self.assertIsNotNone(result)
        self.assertTrue(result.name == 'newone')

    def test_delete_access_level_by_id(self):
        """ Тест функции удаления записи AccessLevel по id """
        AccessLevelService.delete_access_level_by_id(_id=1)
        result = AccessLevelService.get_access_level_by_id(_id=1)
        self.assertIsNone(result)

    def tearDown(self):
        pass


class AccountServerAccessLevelTestCase(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        AccountService.create_account(_username='first', _email='first', _password='0')
        ServerDataService.create_server_data(_name='first', _ip='first', _port=0)
        AccessLevelService.create_access_level(_level=1, _name='zero')
        AccountServerAccessLevelService.create_account_server_access_level(_account=1, _server=1, _access_level=1)

    def test_get_account_access_level_by_account(self):
        """ Тест функции поиска записи AccountAccessLevel по аккаунту """
        result = AccountServerAccessLevelService.get_account_server_access_level_by_account(_account=1)
        for row in result:
            print(row)
            self.assertIsNotNone(row)
            self.assertTrue(row.account.username == 'first')
            self.assertTrue(row.access_level.name == 'zero')

    def test_get_account_access_level_by_server(self):
        """ Тест функции поиска записи ServerAccessLevel по серверу """
        result = AccountServerAccessLevelService.get_account_server_access_level_by_server(_server=1)
        for row in result:
            print(row)
            self.assertIsNotNone(row)
            self.assertTrue(row.server.name == 'first')
            self.assertTrue(row.access_level.name == 'zero')

    def test_get_account_access_level_by_access_level(self):
        """ Тест функции поиска записи AccountAccessLevel по уровню доступа """
        result = AccountServerAccessLevelService.get_account_server_access_level_by_access_level(_access_level=1)
        for row in result:
            print(row)
            self.assertIsNotNone(row)
            self.assertTrue(row.account.username == 'first')
            self.assertTrue(row.access_level.name == 'zero')

    def test_get_account_access_level_by_id(self):
        """ Тест функции поиска записи AccountAccessLevel по id """
        result = AccountServerAccessLevelService.get_account_server_access_level_by_id(_id=1)
        print(result)
        self.assertIsNotNone(result)
        self.assertTrue(result.account.username == 'first')
        self.assertTrue(result.access_level.name == 'zero')

    def test_delete_account_access_level_by_id(self):
        """ Тест функции удаления записи AccountAccessLevel по id """
        AccountServerAccessLevelService.delete_account_server_access_level_by_id(_id=1)
        result = AccountServerAccessLevelService.get_account_server_access_level_by_id(_id=1)
        self.assertIsNone(result)

    def tearDown(self):
        pass
