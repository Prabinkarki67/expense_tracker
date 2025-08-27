from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
# Create your views here.

def index(request):
    return render(request, 'expenses/index.html')
def register(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
    else:
        form=UserRegisterForm()
    return render(request, 'expenses/register.html', {'form': form})