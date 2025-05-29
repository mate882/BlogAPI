from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import get_user_model
from django.contrib import messages

# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.user.is_authenticated and request.user.is_verified:
        return redirect('home')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home') 
        
        else:
            messages.error(request, "❌ There is something wrong with your input.")
    else:
        form = RegisterForm()
    
    return render(request, 'main/register.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('register')

def home(request):
    return render(request, 'main/home.html')

