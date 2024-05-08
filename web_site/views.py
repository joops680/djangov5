from django.shortcuts import render

# Create your views here. 


def home(request):
    """
    Render the home.html template for user registration.

    Parameters:
    - request: HttpRequest object

    Returns:
    - Rendered HttpResponse object
    """
    return render(request, "home.html")


def about(request):
    """
    Render the about.html template for user registration.

    Parameters:
    - request: HttpRequest object

    Returns:
    - Rendered HttpResponse object
    """ 
    return render(request, "about.html")


def learn(request):
    """
    Render the learn.html template for user registration.

    Parameters:
    - request: HttpRequest object

    Returns:
    - Rendered HttpResponse object
    """
    return render(request, "learn.html")

def login_user(request):
    """
    Render the login_user.html template for user registration.

    Parameters:
    - request: HttpRequest object

    Returns:
    - Rendered HttpResponse object
    """
    return render(request, "login.html")