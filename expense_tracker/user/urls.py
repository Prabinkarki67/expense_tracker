from . import views
from django.urls import path

urlpatterns  = [
    path('login/', views.login_user, name='login'),
    path("user/", views.user_page, name='user_page'),
    path('addexpense/', views.add_expense, name='add_expense')
]