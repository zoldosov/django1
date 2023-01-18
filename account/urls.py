from django.urls import path
from .views import register_user, login_user, logout_user

app_name = 'account'

urlpatterns = [
    path('registration/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout')
]