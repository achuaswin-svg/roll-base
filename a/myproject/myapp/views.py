from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.http import HttpResponseForbidden
from .forms import RegistrationForm, LoginForm
from .models import CustomUser

# View for guests
def guest_view(request):
    return render(request, 'guest.html')

# View for users
def user_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.user.role == 'admin':
        return redirect('admin_dashboard')  # Redirect admin to admin dashboard if they access user dashboard
    return render(request, 'user_dashboard.html', {'username': request.user.username})

def admin_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.user.role != 'admin':
        return redirect('user_dashboard')
    return render(request, 'admin_dashboard.html')



def home_view(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = CustomUser.objects.filter(username=username).first()  # Use .filter() and .first() for safer query
            if user and user.check_password(form.cleaned_data.get('password')):
                auth_login(request, user)
                if user.role == 'admin':
                    return redirect('admin_dashboard')
                else:
                    return redirect('user_dashboard')
            else:
                return redirect('login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db() 
            user.role = form.cleaned_data.get('role')
            user.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})