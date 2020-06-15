from django.db import models
from django.contrib.auth.models import User

default_url = "profile2.png"

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True)
    profile_picture = models.ImageField(default=default_url, null=True, blank=True)
    first_name = models.CharField(max_length=200,null=True, default="Информация отсутствует")
    last_name = models.CharField(max_length=200,null=True, default="Информация отсутствует")
    email = models.CharField(max_length=200, null=True, default="Информация отсутствует")
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username
    @property
    def get_comments_count(self):
        return self.user.comment_set.all().count()

    @property
    def get_post_count(self):
        return self.user.author.all().count()
