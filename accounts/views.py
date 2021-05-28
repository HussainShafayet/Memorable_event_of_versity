from django.shortcuts import render, redirect
from accounts.forms import Register, UserLoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def home(request):
    if request.user.is_authenticated:

        return render(request, 'home.html')
    else:
        return redirect('login')


def about(request):
    return render(request, 'about.html')

# User_Registration


def sign_up(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_staff = True
            user.save()
            messages.success(request, 'Account Created Successfully.')
            return redirect('login')
        else:
            context = {
                'form': form,
            }
            return render(request, 'register.html', context)
    else:
        form = Register()
        context = {
            'form': form,
        }
        return render(request, 'register.html', context)


# User Login
def user_login(request):
    if request.method == 'POST':
        log_form = UserLoginForm(request.POST)
        if log_form.is_valid():
            username = log_form.cleaned_data['username']
            password = log_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Login Successfully')
                return redirect('/')
            else:
                messages.warning(request, 'Username or Password Incorrect')
                context = {
                    'log_form': UserLoginForm(),

                }
                return render(request, 'login.html', context)
        else:
            messages.warning(request, 'Username or Password Incorrect')
            context = {
                'log_form': UserLoginForm(),

            }
            return render(request, 'login.html', context)
    else:
        log_form = UserLoginForm()
        context = {
            'log_form': log_form
        }
    return render(request, 'login.html', context)


def user_logout(request):
    logout(request)
    messages.warning(request, 'You are logged out')
    return redirect('/')


