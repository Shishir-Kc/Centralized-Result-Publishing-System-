from django.urls import path
from .views import user_login,user_register,home

app_name = "accounts"

urlpatterns = [
    path('',home,name='home'),
    path('accounts/login/',user_login,name='user_login'),
    path('accounts/register/',user_register,name='user_register')
]
