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

def manage_savings_goal(request, goal_id=None):
    if goal_id:
        # Update or delete a specific goal
        goal = get_object_or_404(SavingsGoal, pk=goal_id)
    else:
        # Create a new goal
        goal = None

    if request.method == 'POST':
        form = SavingsGoalForm(request.POST, instance=goal)
        if 'delete' in request.POST:
            # Handle delete
            if goal:
                goal.delete()
            return redirect('manage_savings_goal')  # Redirect to the list or create page

        if form.is_valid():
            savings_goal = form.save(commit=False)
            if goal is None:  # Only set the user if creating a new goal
                savings_goal.user = request.user
            savings_goal.save()
            return redirect('manage_savings_goal')  # Redirect to the list or create page

    else:
        form = SavingsGoalForm(instance=goal)

    # Fetch all goals for the logged-in user
    goals = SavingsGoal.objects.filter(user=request.user)

    return render(request, 'savings_goals.html', {'form': form, 'goals': goals})

def delete_goals(request):
    if request.method == 'POST':
        goals_to_delete = request.POST.getlist('goals_to_delete')
        SavingsGoal.objects.filter(id__in=goals_to_delete).delete()
    return redirect('manage_goal_create')