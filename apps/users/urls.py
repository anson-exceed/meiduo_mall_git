from django.urls import path
from . import views


from apps.users.views import UsernameCountView

urlpatterns = [
    # 判断用户名是否重复
    path('usernames/<username:username>/count/',views.UsernameCountView.as_view()),
]
