from django.urls import path
from .views import *

app_name = "post"

urlpatterns = [
    path('', post_list, name='post_list'),
    path("<slug:slug>", post_detail, name="post_detail"),
    path("create/<slug:slug>", post_create, name="post_create"),
]
