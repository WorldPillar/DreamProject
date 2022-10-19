from django.db.models import *

# Create your models here.


class Account(Model):
    id = AutoField(primary_key=True)
    username = CharField(max_length=255, null=False, unique=True)
    email = CharField(max_length=255, null=False, unique=True)
    password = CharField(max_length=255, null=False)

    class Meta:
        db_table = 'account'

    def __str__(self):
        return str({'id': self.id, 'username': self.username, 'email': self.email})


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
    level = IntegerField(null=False, unique=True)
    name = CharField(max_length=255, null=False, unique=True)

    class Meta:
        db_table = 'access_level'

    def __str__(self):
        return str({'id': self.id, 'level': self.level, 'name': self.name})


class FriendList(Model):
    id = AutoField(primary_key=True)
    owner = ForeignKey('Account', null=False, on_delete=CASCADE, related_name='owner')
    friend = ForeignKey('Account', null=False, on_delete=CASCADE, related_name='friend')

    class Meta:
        db_table = 'friend_list'
        """ Объявление составного уникального значения по полям owner и friend """
        unique_together = ('owner', 'friend')

    def __str__(self):
        return str({'id': self.id, 'owner': self.owner, 'friend': self.friend})


class NewsData(Model):
    id = AutoField(primary_key=True)
    date = DateTimeField(auto_now_add=True)
    author = ForeignKey('Account', null=True, on_delete=SET_NULL)
    topic = CharField(max_length=255, null=False)
    text = TextField(null=False)

    class Meta:
        db_table = 'news_data'

    def __str__(self):
        return str({'id': self.id, 'date': self.date, 'author': self.author,
                    'topic': self.topic, 'text': self.text})


class AccountAccessLevel(Model):
    id = AutoField(primary_key=True)
    account = ForeignKey('Account', null=False, on_delete=CASCADE)
    access_level = ForeignKey('AccessLevel', null=False, on_delete=CASCADE)

    class Meta:
        db_table = 'account_access_level'
        """ Объявление составного уникального значения по полям account и access_level """
        unique_together = ('account', 'access_level')

    def __str__(self):
        return str({'id': self.id, 'account': self.account, 'access_level': self.access_level})


class ServerAccessLevel(Model):
    id = AutoField(primary_key=True)
    server = ForeignKey('ServerData', null=False, on_delete=CASCADE)
    access_level = ForeignKey('AccessLevel', null=False, on_delete=CASCADE)

    class Meta:
        db_table = 'server_access_level'
        """ Объявление составного уникального значения по полям server и access_level """
        unique_together = ('server', 'access_level')

    def __str__(self):
        return str({'id': self.id, 'server': self.server, 'access_level': self.access_level})
