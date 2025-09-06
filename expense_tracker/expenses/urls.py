from . import views
from django.urls import path
from user import views as user_views

urlpatterns  = [
    path('', views.index, name='index'),
    path('addexpense/', user_views.add_expense, name='add_expense'),
]