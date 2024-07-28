from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('logout/', views.logoutUser, name='logout'), 
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('manage/', views.manage_savings_goals, name='manage_savings_goals'),
    path('update/<int:pk>/', views.update_savings_goal, name='update_savings_goal'),
    path('delete/<int:pk>/', views.delete_savings_goal, name='delete_savings_goal'),
]
