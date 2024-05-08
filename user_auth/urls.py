from django.urls import path
from . import views

app_name = 'user_auth'
urlpatterns = [
    path('', views.login_user, name='login_user'),
    path('user_register', views.user_register, name='user_register'),
    path('authenticate_user', views.authenticate_user, name='authenticate_user'),
]