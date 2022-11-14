from django.db.models import *
from django.contrib.auth import get_user_model

User = get_user_model()


# class Account(Model):
#     id = AutoField(primary_key=True)
#     username = CharField(max_length=255, null=False, unique=True)
#     email = CharField(max_length=255, null=False, unique=True)
#     password = CharField(max_length=255, null=False)
#
#     class Meta:
#         db_table = 'account'
#
#     def __str__(self):
#         return str({'id': self.id, 'username': self.username, 'email': self.email})


class ServerData(Model):
    id = AutoField(primary_key=True)
    ip = CharField(max_length=15, null=False)
    port = IntegerField(null=False)
    name = CharField(max_length=255, null=False, unique=True)

    class Meta:
        db_table = 'server_data'
        """ Объявление составного уникального значения по полям ip и port """
        unique_together = ('ip', 'port')

    def __str__(self):
        return str({'id': self.id, 'ip': self.ip, 'port': self.port, 'name': self.name})


class AccessLevel(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=255, null=False, unique=True)

    class Meta:
        db_table = 'access_level'

    def __str__(self):
        return str({'id': self.id, 'name': self.name})


class ServiceAccessLevel(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=255, null=False, unique=True)

    class Meta:
        db_table = 'service_access_level'

    def __str__(self):
        return str({'id': self.id, 'name': self.name})


class FriendList(Model):
    id = AutoField(primary_key=True)
    owner = ForeignKey(
        User,
        null=False,
        on_delete=CASCADE,
        related_name='owner'
    )
    friend = ForeignKey(
        User,
        null=False,
        on_delete=CASCADE,
        related_name='friend'
    )
    # owner = ForeignKey('Account', null=False, on_delete=CASCADE, related_name='owner')
    # friend = ForeignKey('Account', null=False, on_delete=CASCADE, related_name='friend')

    class Meta:
        db_table = 'friend_list'
        """ Объявление составного уникального значения по полям owner и friend """
        unique_together = ('owner', 'friend')

    def __str__(self):
        return str({'id': self.id, 'owner': self.owner, 'friend': self.friend})


class NewsData(Model):
    id = AutoField(primary_key=True)
    date = DateTimeField(auto_now_add=True)
    author = ForeignKey(
        User,
        null=True,
        on_delete=SET_NULL
    )
    # author = ForeignKey('Account', null=True, on_delete=SET_NULL)
    topic = CharField(max_length=255, null=False)
    text = TextField(null=False)

    class Meta:
        db_table = 'news_data'

    def __str__(self):
        return str({'id': self.id, 'date': self.date, 'author': self.author,
                    'topic': self.topic, 'text': self.text})


class AccountServerAccessLevel(Model):
    id = AutoField(primary_key=True)
    account = ForeignKey(
        User,
        null=False,
        on_delete=CASCADE
    )
    # account = ForeignKey('Account', null=False, on_delete=CASCADE)
    server = ForeignKey('ServerData', null=False, on_delete=CASCADE)
    access_level = ForeignKey('AccessLevel', null=False, on_delete=CASCADE)

    class Meta:
        db_table = 'account_server_access_level'
        """ Объявление составного уникального значения по полям account и access_level """
        unique_together = ('account', 'server', 'access_level')

    def __str__(self):
        return str({'id': self.id, 'account': self.account, 'server': self.server, 'access_level': self.access_level})


class AccountServiceAccessLevel(Model):
    id = AutoField(primary_key=True)
    account = ForeignKey(
        User,
        null=False,
        on_delete=CASCADE
    )
    # account = ForeignKey('Account', null=False, on_delete=CASCADE)
    access_level = ForeignKey('ServiceAccessLevel', null=False, on_delete=CASCADE)

    class Meta:
        db_table = 'account_service_access_level'

    def __str__(self):
        return str({'id': self.id, 'account': self.account, 'access_level': self.access_level})
