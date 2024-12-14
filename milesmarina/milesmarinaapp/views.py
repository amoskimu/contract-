from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def contact(request):
    return render(request, 'contact.html')

def login_register(request):
    if request.method == "POST":
        if "login" in request.POST:  # Handle Login
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect('home')  # Redirect to home page on successful login
            else:
                messages.error(request, "Invalid username or password.")
        
        elif "register" in request.POST:  # Handle Registration
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists. Please choose a different one.")
            else:
                User.objects.create_user(username=username, email=email, password=password)
                messages.success(request, "Registration successful! You can now log in.")
                return redirect('login')  # Redirect to login/register page to log in

    return render(request, 'login_register.html')
