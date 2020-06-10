from django import forms
from .models import *


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        # self.title['title'].widget.attrs['placeholder'] = self.instance.placeholder
        self.fields['title'].widget.attrs['placeholder'] = 'Заголовок'
        self.fields['slug'].widget.attrs['placeholder'] = 'Название в url строке'

    class Meta:
        model = Post
        fields = ['title', 'slug', 'author', 'category']
        labels = {
            "title" : "Заголовок",
            "slug" : "Слаг",
            "author" : "Автор",
            "category" : "Категория"
        }
