from django.shortcuts import render, redirect
from .models import Post, ArticleContent
from django.core.paginator import Paginator
from django.forms import inlineformset_factory, modelformset_factory

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

def post_create(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    PostFormset = inlineformset_factory(Post, ArticleContent, fields = ('subtitle', 'subtext',), extra = 1)

    if request.method == "POST":
        formset = PostFormset(request.POST, instance = post)
        if formset.is_valid():
            formset.save()
            return redirect('post_create', slug=post.slug)

    formset = PostFormset(instance = post)

    return render(request, "pages/post/post_create.html", {"formset" : formset})


def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, "pages/post/post_detail.html", {"post" : post})




# instances = formset.save(commit=False)
# for instance in instances:
