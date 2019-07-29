from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Create your views here.


def SignUp(request):
    error = ""
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        try:
            User.objects.get(username = username)
        except:
            user = User.objects.create_user(username, email, password)
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.save()
            return render(request, 'auth/afterSignup.html')
        error = "Username already exists"
        context = {
            error: "error"
        }
        return render(request, 'auth/signup.html', context)  
    else:
        return render(request, 'auth/signup.html')
        
    


def UserLogin(request):
    error = ""
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            error = "Incorrect Username or Password"
        context = {
            'error': error
        }
        return render(request, 'auth/login.html', context)
    else:
        return render(request, 'auth/login.html')

def Logout(request):
    logout(request)
    return render(request, 'index.html')
