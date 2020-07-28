from django import forms
from .models import *





class MceForm(forms.ModelForm):
    class Meta:
        model = Mce
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):
    content = forms.CharField(label='Ваш комментарий', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Ваш комментарий...',
        'id': 'usercomment',
        'rows': '4',
    }))

    class Meta:
        model = Comment
        fields = ('content',)


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
