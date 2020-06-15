from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserForm, CustomUserSettingsForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import CustomUser





def profile_user(request, username):
    user = User.objects.get(username=username)
    profile = CustomUser.objects.get(user=user)
    context = {"profile" : profile}
    return render(request, "account/profile_user.html", context)

def settings_profile(request):
    current_user = request.user.customuser
    form = CustomUserSettingsForm(instance=current_user)

    if request.method == 'POST':
        form = CustomUserSettingsForm(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save()
            return redirect(reverse("account:profile_user", kwargs={'username': current_user.name}))

    return render(request, "pages/test.html", {"form" : form})


def register_user(request):
    if request.user.is_authenticated:
        return redirect("post:post_list")
    else:
        form = CustomUserForm()

        if request.method == "POST":
            form = CustomUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                # CustomUser.objects.create(user=new_user)
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
