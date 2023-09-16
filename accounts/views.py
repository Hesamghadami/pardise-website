from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import CustumUser
from django.http import HttpResponseRedirect




def Login(req) :
    if req.user.is_authenticated:
        return redirect('/')
    
    elif req.method == 'GET':
        form = AuthenticationForm()

        return render(req, 'registration/login.html', {'form': form})
    
    elif req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(req, user)
            return redirect('/')
        else :
            messages.add_message(req, messages.ERROR , 'username or password is not valid ! ...')
            return redirect('accounts:login')


@login_required
def Logout(req) :
    logout(req)
    return redirect('/')



def signup(req):
    if req.method == 'GET':
        form = SignUpForm()
        return render(req, 'registration/signup.html', {'form': form})
    
    elif req.method == 'POST':
            form = SignUpForm(req.POST, req.FILES)
            print (req.POST)
            if form.is_valid():
                form.save()
                return redirect('accounts:login')
        
            else:
                messages.add_message(req,messages.ERROR,'Input data is not valid.')
                return redirect('accounts:login')
