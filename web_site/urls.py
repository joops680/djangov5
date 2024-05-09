from django.urls import path, include
from . import views

"""
URL patterns for the application.

login_user: Displays a login form for the user.
user_register: Displays a user registration form.
home: Displays the home page.
about: Displays the about page.
learn: Displays the learn page.
user_auth: Includes URL patterns for authentication views provided by Django's contrib.auth app.
user_auth: Includes URL patterns for views provided by the 'user_auth' app.

"""
urlpatterns = [ 
    path('', views.login_user, name='login_user'),
    #path('user_register/', views.user_register, name='user_register'),
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("learn/", views.learn, name="learn"),
    path("user_auth/", include("django.contrib.auth.urls")),
    path("user_auth/", include("user_auth.urls")),   

]