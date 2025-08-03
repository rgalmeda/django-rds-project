from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import SignupForm


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Wrong Username or Password")
            return redirect('login')

    return render(request, 'authenticate/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login')


def register_user(request):
    form = SignupForm(request.POST)
    if form.is_valid():
        form.save()

        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']

        user = authenticate(request, username=username, password=password)
        login(request, user)
        messages.success(request, "registered successfully")
        return redirect('index')
    else:
        messages.error(request, "Error occurred during registration")
    return render(request, 'authenticate/signup.html', {"form": form})
