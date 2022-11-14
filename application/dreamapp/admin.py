from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(ServerData)
admin.site.register(AccessLevel)
admin.site.register(FriendList)
admin.site.register(NewsData)
admin.site.register(AccountServerAccessLevel)
admin.site.register(AccountServiceAccessLevel)
admin.site.register(ServiceAccessLevel)
