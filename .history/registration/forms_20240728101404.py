from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import SavingsGoal, Contribution

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class SavingsGoalForm(forms.ModelForm):
    class Meta:
        model = SavingsGoal
        fields = ['name', 'target_amount', 'target_date']
        widgets = {
            'target_date': forms.DateInput(attrs={'type': 'date'}),
        }

# Form is for making a contribution to a savings goal
class ContributionForm(forms.ModelForm):
    class Meta:
        model = Contribution
        fields = ['savings_goal', 'amount']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ContributionForm, self).__init__(*args, **kwargs)
        if user:
            # Limiting the savings goal choices to those belonging to the current user
            self.fields['savings_goal'].queryset = SavingsGoal.objects.filter(user=user)