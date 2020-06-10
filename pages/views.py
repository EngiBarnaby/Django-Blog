from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.core.paginator import Paginator
from django.forms import inlineformset_factory, modelformset_factory
from .forms import PostForm
from django.views.generic.base import View
from django.forms.models import modelform_factory
from django.db.models import Count, Q

def search(request):
    posts = Post.objects.all()
    query = request.GET.get('main-search')
    if query:
        queryset = Post.objects.filter(title__icontains=query).distinct()

    context = {"queryset" : queryset}
    return render(request, "pages/post/search_result.html", context)

def post_list(request, category_id=None, tag_id=None):
    tag = None
    category = None
    posts = Post.objects.all()
    categories = Category.objects.all()

    if tag_id:
        tag = get_object_or_404(Tag, id=tag_id)
        posts = Post.objects.filter(tags=tag)

    if category_id:
        category = get_object_or_404(Category, id=category_id)
        posts = Post.objects.filter(category=category)

    pages = Paginator(posts, 8)

    if "page" in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1

    page = pages.get_page(page_num)

    context = {'all_post' : page.object_list, 'page' : page, "categories" : categories}
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
