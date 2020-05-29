from django.contrib import admin
from .models import *

# class ArticleContentLine(admin.TabularInline):
#     model = ArticleContent
#     extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish')
    prepopulated_fields = {'slug': ('title',)}
    # inlines = [
    #     ArticleContentLine,
    # ]
