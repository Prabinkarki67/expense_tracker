from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Expense
from django.db.models import Sum 


import matplotlib
import matplotlib.pyplot as plt
import io, base64

matplotlib.use('Agg')  # Prevent GUI errors




@login_required
def user_page(request):
    expenses = Expense.objects.filter(user=request.user)
    total = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    
    category_data = (
        expenses.values('category')
        .annotate(total=Sum('amount'))
        .order_by('category')
    )
    categories = [item['category'] for item in category_data]
    category_totals = [float(item['total']) for item in category_data]    
    fig, ax = plt.subplots()
    ax.pie(category_totals, labels = categories, autopct = '%1.1f%%', startangle = 90)
    ax.axis('equal')
    
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png).decode('utf-8')    
    
    return render(request, 'user/user.html', {
        'user':request.user,
        'expenses': expenses, 
        'total': total,
        'graphic': graphic})


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
            return redirect('user_page') 
    return render(request, 'user/add_exp.html')