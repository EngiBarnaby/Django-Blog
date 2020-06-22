from django.urls import path
from .views import *

app_name = "post"

urlpatterns = [
    path('', post_list, name='post_list'),
    path('tag_filter/<str:tag_slug>', post_list, name="post_list_by_tag"),
    path('category_filter/<int:category_id>', post_list, name='post_list_by_category'),
    path('search', search, name="search"),
    path("detail/<slug:slug>", post_detail, name="post_detail"),
    path("create/", post_create, name="post_create"),
    path("update/<slug:slug>", post_update, name="post_update"),
    path('delete/<slug:slug>', post_delete, name="post_delete"),
    path("test", tinymce, name="tinymce"),
    # path("update2/<slug:slug>", PostUpdate.as_view(), name="post_update2"),
]
