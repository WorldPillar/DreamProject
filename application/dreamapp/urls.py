from .views.friendlist_view import FriendListPostDeleteAPIView, FriendListGetAPIView
from .views.news_view import NewsGetAPIView, NewsPostAPIView, NewsDeleteAPIView
from .views.server_view import ServerDataGetAPIView, ServerDataPostAPIView, ServerDataDeleteAPIView, ServerDataUpdateAPIView

from django.urls import path

urlpatterns = [
    # news api
    path('news', NewsGetAPIView.as_view()),
    path('news/post', NewsPostAPIView.as_view()),
    path('news/delete/<int:pk>', NewsDeleteAPIView.as_view()),
    # friendlist api
    path('friendlist/<str:friend>', FriendListPostDeleteAPIView.as_view()),
    path('friendlist/', FriendListGetAPIView.as_view()),
    # server api
    path('server', ServerDataGetAPIView.as_view()),
    path('server/post', ServerDataPostAPIView.as_view()),
    path('server/update/<int:pk>', ServerDataUpdateAPIView.as_view()),
    path('server/delete/<int:pk>', ServerDataDeleteAPIView.as_view())
]
