from django.urls import path
from .views import *

app_name = "post"

urlpatterns = [
    path('', post_list, name='post_list'),
    path("<slug:slug>", post_detail, name="post_detail"),
    path("create/", post_create, name="post_create"),
    path("update/<slug:slug>", post_update, name="post_update"),
    path("update2/<slug:slug>", PostUpdate.as_view(), name="post_update2"),
]
