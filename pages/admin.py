from django.contrib import admin
from .models import *
from ckeditor.widgets import CKEditorWidget
# class ArticleContentLine(admin.TabularInline):
#     model = ArticleContent
#     extra = 1

class ArticleContentInline(admin.StackedInline):
    model = ArticleContent

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ArticleContentInline]
    # inlines = [
    #     ArticleContentLine,
    # ]
