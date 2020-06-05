from django.shortcuts import render
from django.contrib.auth import authenticate,
from djago.contrib.auth.form import UserCreationForm


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

# @login_required
# def dashboard(request):
#     return render(request,'pages/base.html',{'section': 'dashboard'})
