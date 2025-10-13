from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Expense



    
@login_required
def user_page(request):
    return render(request, 'user/user.html', {'user':request.user})


def login_user(request):
    if request.method=='POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
                login(request, user)
                return redirect('user_page')
        else:
            messages.error(request, 'Invalid Login')
            return redirect('login')
    else:
        return render(request, 'user/login.html')

@login_required
def add_expense(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        amount = request.POST.get('amount')

        if category and amount:
            Expense.objects.create(
                user=request.user, 
                category=category,
                amount=amount
            )
            return redirect('dashboard') 
    return render(request, 'user/add_exp.html')