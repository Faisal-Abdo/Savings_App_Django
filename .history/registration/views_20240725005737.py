from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from .models import SavingsGoal
from .forms import SavingsGoalForm

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
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password')
    return render(request, 'authentication/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def manage_savings_goals(request):
    if request.method == "POST":
        form = SavingsGoalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_savings_goals')
    else:
        form = SavingsGoalForm()

    goals = SavingsGoal.objects.all()
    return render(request, 'savings_goals.html', {'form': form, 'goals': goals})

def update_savings_goal(request, pk):
    goal = get_object_or_404(SavingsGoal, pk=pk)
    if request.method == "POST":
        form = SavingsGoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect('manage_savings_goals')
    else:
        form = SavingsGoalForm(instance=goal)
    return render(request, 'update_goal.html', {'form': form, 'goal': goal})

def delete_savings_goal(request, pk):
    goal = get_object_or_404(SavingsGoal, pk=pk)
    if request.method == "POST":
        goal.delete()
        return redirect('manage_savings_goals')
    return render(request, 'delete_goal.html', {'goal': goal})