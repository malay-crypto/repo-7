from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.


def index(req):
    return render(req,'app1/index.html')

def loginPage(req):
    return render(req, 'app1/login.html')


def register(req):
    return render(req, 'app1/registration.html')

def loginValidation(req):
    if req.method == 'POST':
        uname = req.POST['uname']
        password = req.POST['password']

        try:
            u = User.objects.get(username=uname)


            if u.check_password(password):
                    return render(req, 'app1/Home.html')
            else:
                    return render(req,'app1/login.html',{'mess':'Invalid user id or password'})
        except:
                try:
                    u = User.objects.get(email=uname)

                    return render(req, 'app1/Home.html')
                except:
                    return render(req,'app1/login.html',{'mess':'Invalid user id or email'})

def signUp(req):
    if req.method=='POST':
        uname = req.POST['uname']
        email=req.POST['email']
        password = req.POST['password']
        password2 = req.POST['password2']

        if password!=password2:
            return render(req, 'app1/registration.html',{'mess':'password mismatch'})
        else:

            u=User(username=uname,email=email,password=make_password(password))
            u.save()
            return redirect('/login')

    else:
        return render(req, 'app1/registration.html')

@login_required
def home(req):
    return render(req, 'app1/Home.html')

@login_required
def form(req):
    return render(req, 'app1/cst.html')

@login_required
def inventory(req):
    return render(req, 'app1/cst1.html')

def logout_view(req):
    response = HttpResponse('cookie')
    response.delete_cookie('user')
    logout(req)
    return redirect('/login')