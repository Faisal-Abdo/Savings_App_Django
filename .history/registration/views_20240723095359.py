from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'templates/home.html') 

def register(request):
    return render(request, 'authentication/register.html')

def login_view(request):
    return render(request, 'authentication/login.html')