from django.db import models

# My models/database are here.

from django.contrib.auth.models import User

class SavingsGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='savings_goals')
    name = models.CharField(max_length=50)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    target_date = models.DateField()

#just a string representation:
    def __str__(self):
        return self.name
    
# Model to represent a contribution to a savings goal
class Contribution(models.Model):
    savings_goal = models.ForeignKey(SavingsGoal, related_name='contributions', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.amount} to {self.savings_goal.goal_name} on {self.date}"
