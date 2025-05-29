from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, authenticate, logout
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
        form = RegisterForm()
    
    return render(request, 'main/register.html', {'form': form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid Email or password')
    else:
        form = LoginForm()

    return render(request, 'main/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('register')

def home(request):
    return render(request, 'main/home.html')

