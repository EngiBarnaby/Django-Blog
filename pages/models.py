from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("post:post_list_by_tag", args=[self.id])

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категорий'

    def get_absolute_url(self):
        return reverse("post:post_list_by_category", args=[self.id])

class Post(models.Model):
    title = models.CharField(max_length=100)
    # subtitle = models.CharField(max_length=100)
    # subtext = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    slug = models.SlugField(unique=True)
    image = models.ImageField(null=True, blank=True)
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='tags')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-publish",)
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьй'

    def get_absolute_url(self):
        return reverse("post:post_detail", args=[self.slug])

class ArticleContent(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="paragraphs")
    subtitle = models.CharField(max_length=100)
    subtext = RichTextField()

    def __str__(self):
        return self.subtitle
