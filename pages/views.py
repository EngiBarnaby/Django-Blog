from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator

def post_list(request):
    all_post = Post.objects.all()
    pages = Paginator(all_post, 2)

    if "page" in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1

    page = pages.get_page(page_num)

    context = {'all_post' : page.object_list, 'page' : page}
    return render(request, "pages/post/post_list.html", context)
