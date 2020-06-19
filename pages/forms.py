from django import forms
from .models import *





class MceForm(forms.ModelForm):
    class Meta:
        model = Mce
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):
    # content = forms.CharField(label='Ваш комментарий', widget=forms.Textarea(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'Ваш комментарий...',
    #     'id': 'usercomment',
    #     'rows': '4',
    # }))

    class Meta:
        model = Comment
        fields = ('content',)


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        # self.title['title'].widget.attrs['placeholder'] = self.instance.placeholder
        self.fields['title'].widget.attrs['placeholder'] = 'Заголовок'
        self.fields['title_text'].widget.attrs['placeholder'] = 'Краткий текст про статью'
        self.fields['slug'].widget.attrs['placeholder'] = 'Название в url строке'

    class Meta:
        model = Post
        fields = ['title', "title_text",'slug','category']
        labels = {
            "title" : "Заголовок",
            "title_text" : "Краткий текст",
            "slug" : "Слаг",
            "category" : "Категория"
        }
