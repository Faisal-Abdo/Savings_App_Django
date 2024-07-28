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
