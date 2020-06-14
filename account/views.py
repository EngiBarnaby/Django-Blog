from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserForm, CustomUser
from django.contrib import messages


def settings_profile(request):
    current_user = request.user.customuser
    form = CustomUser(instance=current_user)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES,instance=customer)
        if form.is_valid():
                form.save()
    return render(request, "pages/test.html", {"form" : form})


def register_user(request):
    if request.user.is_authenticated:
        return redirect("post:post_list")
    else:
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
    if request.user.is_authenticated:
        return redirect("post:post_list")
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("post:post_list")
            else:
                messages.info(request, "Имя или пароль неверны")

        return render(request, "account/login_user.html", {})

def logout_user(request):
    logout(request)
    return redirect('account:login')

# @login_required
# def dashboard(request):
#     return render(request,'pages/base.html',{'section': 'dashboard'})
