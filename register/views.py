from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate

# Create your views here.


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/home")
    else:
        form = RegisterForm()
            
    return render(response , "register/register.html", {"form": form})

def login_view(response):
    if response.method == "POST":
        form = LoginForm(response.POST)
        username = response.POST.get("username")
        password = response.POST.get("password")
        print(response.POST.get("username"), response.POST.get("password"))
        
        user = authenticate(response, username = username, password = password)
        if user is None:
            context = {"error" : "Invalid username or password!",
                       "form" : form}
            return render(response, "register/login.html", context)
        login(response, user)
        return redirect("/home")
    
    else:
        form = LoginForm()
        
    return render(response, 'register/login.html', {"form" : form})