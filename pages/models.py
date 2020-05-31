from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=100)
    # subtitle = models.CharField(max_length=100)
    # subtext = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    slug = models.SlugField(unique=True)
    image = models.ImageField(null=True, blank=True)
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    tags = TaggableManager()


    def __str__(self):
        return self.title

class ArticleContent(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="paragraphs")
    subtitle = models.CharField(max_length=100)
    subtext = RichTextField()

    def __str__(self):
        return self.subtitle
