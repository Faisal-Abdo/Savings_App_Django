from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('logout/', views.logoutUser, name='logout'), 
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('create-goal/', views.manage_savings_goal, name='manage_savings_goal'),
    path('manage-goal/<int:id>/', views.manage_savings_goal, name='manage_savings_goal'),
    path('delete-goals/', views.delete_goals, name='delete_goals'),
]
