from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('logout/', views.logoutUser, name='logout'), 
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('create-goal/', views.manage_savings_goal, name='manage_savings_goal'),
    path('manage-goal/<int:goal_id>/', views.manage_savings_goal, name='manage_savings_goal'), #the parameter(goal_id) name matches the view function
    path('delete-goals/', views.delete_goals, name='delete_goals'),
    path('contribute/', views.contribute, name='contribute'),
    path('goal-details/<int:goal_id>/', views.goal_details, name='goal_details'),
    path('progress/', views.progress, name='progress'),
]
