from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('logout/', views.logoutUser, name='logout'), 
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('manage-goal/', views.manage_savings_goal, name='manage_goal_create'),
    path('manage-goal/<int:goal_id>/', views.manage_savings_goal, name='manage_goal'),
