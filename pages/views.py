from django.shortcuts import render
from .models import Post

def post_list(request):
    all_post = Post.objects.all()
    context = {'all_post' : all_post}
    return render(request, "pages/post/post_list.html", context)
