from django.contrib import admin
from .models import *
from ckeditor.widgets import CKEditorWidget
# class ArticleContentLine(admin.TabularInline):
#     model = ArticleContent
#     extra = 1

class ArticleContentInline(admin.StackedInline):
    model = ArticleContent


admin.site.register(Mce)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(ArticleContent)
# @admin.register(Tag)
# class TagsAdmin(admin.ModelAdmin):
#     list_display = ("name")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ArticleContentInline]
    # inlines = [
    #     ArticleContentLine,
    # ]
