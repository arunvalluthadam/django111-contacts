from django.shortcuts import render

# Create your views here.
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

    )
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .forms import UserLoginForm, UserRegisterForm, EditProfileForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm

def login_view(request):
    print(request.user.is_authenticated())
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/posts")
    return render(request, "form.html", {"form":form, "title": title})


def register_view(request):
    print(request.user.is_authenticated())
    title = "Register"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect("/")

    context = {
        "form": form,
        "title": title
    }
    return render(request, "form.html", context)


def logout_view(request):
    logout(request)
    return redirect("/posts")

def search_view(request):
    
    if request.POST:
        search_text = request.POST['search_text']
    else:
        search_text = ''
    articles = Article.objects.filter(title__contains=search_text)
    return render(request, 'article/ajax_search.html', {'articles': articles})

