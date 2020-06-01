from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.core.paginator import Paginator
from django.forms import inlineformset_factory, modelformset_factory
from .forms import PostForm
from django.views.generic.base import View
from django.forms.models import modelform_factory

def post_list(request):
    all_post = Post.objects.all()
    pages = Paginator(all_post, 8)

    if "page" in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1

    page = pages.get_page(page_num)

    context = {'all_post' : page.object_list, 'page' : page}
    return render(request, "pages/post/post_list.html", context)

def post_create(request):
    if request.method == "GET":
        post_form = PostForm()
        return render(request, 'pages/post/post_create.html', {"post_form" : post_form})
    else:
        post_form = PostForm(request.POST)
        if post_form.is_valid:
            post_form.save()
            return redirect("post:post_update", slug=request.POST["slug"])
        else:
            post_form = PostForm(request.POST)
            return render(request, "pages/post/post_create.html", {"post_form" : post_form})


def post_update(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    PostFormset = inlineformset_factory(Post, ArticleContent, fields = ('subtitle', 'subtext',), extra = 1)

    if request.method == "POST":
        formset = PostFormset(request.POST, instance = post)
        if formset.is_valid():
            formset.save()
            return redirect('post:post_update', slug=post.slug)

    formset = PostFormset(instance = post)

    return render(request, "pages/post/post_update.html", {"formset" : formset})


def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, "pages/post/post_detail.html", {"post" : post})


def post_delete(request, slug):
    article = Post.objects.get(slug__iexact=slug)
    article.delete()
    return redirect("post:post_list")

class PostUpdate(View):
    post = None

    def get_type_content(self, type_name, *args, **kwargs):
        Form = modelform_factory(type_name, exclude=('what',))

    def dispatch(self, request, slug, type_name=ArticleContent):
        self.post = get_object_or_404(Post, slug__iexact=slug)
        return super(PostUpdate,self).dispatch(request, slug, type_name)


    def get(self, request, slug, type_content=ArticleContent):
        PostFormset = self.get_type_content(type_content)
        form = self.get_type_content(type_content, instance=self.post)
        context = {"formset" : form}
        return render(request, "pages/post/post_update2.html", context)

    def post(self, request, post_slug, type_content):
        pass


# instances = formset.save(commit=False)
# for instance in instances:
