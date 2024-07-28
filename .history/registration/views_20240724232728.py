from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 


# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successefully')
            return redirect('login')
    context = {'form': form}
    return render(request, 'authentication/register.html', context)

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username= email, password= password)
        if user is not None:
            login(request, user)
            return redirect('home.html')
        else:
            messages.error(request, 'Invalid email or password')
    return render(request, 'authentication/login.html')