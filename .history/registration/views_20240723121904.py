from django.shortcuts import render
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'templates/home.html')

def register(request):
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'authentication/register.html', context)

def login_view(request):
    return render(request, 'authentication/login.html')