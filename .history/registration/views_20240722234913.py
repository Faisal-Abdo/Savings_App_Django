from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, 'registration\templates\authentication\register.html')

def login_view(request):
    return render(request, 'registration\templates\authentication\login.html')