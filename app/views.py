from django.http import HttpResponse
from django.shortcuts import redirect, render
from . import views
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'app/index.html')

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username = username, password = pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'app/index.html', {'username': username})
        
        else:
            messages.error(request, "credentials do not match")
            return redirect('home')

    return render(request, 'app/signin.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        cname = request.POST['cname']

        if User.objects.filter(username = username):
            messages.error(request, "user already exists")
            return redirect('home')

        if User.objects.filter(email = email):
            messages.error(request, "email already exists")
            return redirect('home')
        
        if pass1 != pass2:
            messages.error(request, "passwords donot match")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request, "username must be alphanumeric")
            return redirect('home')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.company_name = cname

        myuser.save()

        messages.success(request, "account created successfuly!")

        return redirect('signin')

    return render(request, 'app/signup.html')


def hedge(request):
    return render(request, 'app/hedge.html')

def forecast(request):
    return render(request, 'app/forecast.html')

def commodityinfo(request):
    return render(request, 'app/commodityinfo.html')

def signout(request):
    logout(request)
    return redirect('home')