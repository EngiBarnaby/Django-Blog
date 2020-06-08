from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name="account"

urlpatterns = [
    path('register/', register_user, name='register'),
    # path('login/', auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register_done/", register_done, name='register_done'),
    path("login/", login_user, name="login"),
]
