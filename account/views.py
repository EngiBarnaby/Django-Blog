from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserForm

def register_user(request):
    form = CustomUserForm()

    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("account:register_done")

    contex = {"form" : form}
    return render(request, 'account/register.html', contex)

def register_done(request):
    return render(request, "account/register_done.html", {})

def login_user(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("post:post_list")
        else:
            return render(request, 'account/login_user.html')

    else:
        return render(request, "account/login_user.html", {})

# @login_required
# def dashboard(request):
#     return render(request,'pages/base.html',{'section': 'dashboard'})
