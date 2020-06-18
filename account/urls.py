from django.urls import path, reverse_lazy, reverse
from django.shortcuts import reverse
from django.contrib.auth import views as auth_views
from .views import *


app_name="account"

urlpatterns = [
    path('register/', register_user, name='register'),
    # path('login/', auth_views.LoginView.as_view(), name="login"),
    # path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register_done/", register_done, name='register_done'),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("profile_user/<str:username>", profile_user, name="profile_user"),
    path("profile_settings", settings_profile, name="settings_profile"),


    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="account/password_reset.html",
                                        success_url= reverse_lazy("account:password_reset_done"),
                                        email_template_name="account/password_reset_email.html"),
     name="reset_password"),

    path('reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(template_name="account/password_reset_sent.html"),
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="account/password_reset_form.html", success_url= reverse_lazy("account:password_reset_complete")),
     name="password_reset_confirm"),

    path('reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name="account/password_reset_done.html"),
        name="password_reset_complete"),
]
