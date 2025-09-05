from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm

def index(request):
    return render(request, 'expenses/index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():  # automatically checks password1 == password2
            form.save()  # saves the user to the database
            return render(request, 'user/login.html', {'success': 'Account created successfully!'})
        else:
            return render(request, 'expenses/register.html', {'form': form})
    else:
        form = UserRegisterForm()
    return render(request, 'expenses/register.html', {'form': form})
