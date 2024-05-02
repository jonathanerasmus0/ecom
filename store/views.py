import requests
import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Category, Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms
from .utils import get_weather

# Create your views here.





def get_weather(city):
    api_key = '533ac5d37a4fe7dc36dd522b6188abcf'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data







def category(request, foo):
    # replace hypenation with spaces 
    foo = foo.replace('-', ' ')
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html','products:products}', {'category': category})
    except:
        messages.success(request, ("This category doesnt exist! BOO HOO"))
        return redirect('home')





def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html',{'product':product})


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html',{'products':products})

def about(request):
    weather= get_weather(city='London')
    return render(request, 'about.html',{'weather':weather})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, ("you successfully logged in"))
            return redirect ('home')
        else:
            messages.success(request, ("there was an error logging you in "))
            return redirect ('login')
    else:
        return render(request, 'login.html',{})


def logout_user(request):
    logout(request)
    messages.success(request, ("you have been logged out byeeeeee!"))
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request, ("you have registered in Jonathans web store Congratulations!!!"))
            return redirect('home')
        else:
            messages.success(request,("error"))
            return redirect('register')

    return render(request, 'register.html',{'form':form})

