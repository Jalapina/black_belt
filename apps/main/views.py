from django.shortcuts import render, redirect, reverse, HttpResponse
import bcrypt
from django.contrib import messages
from .models import User
import re

REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


def index(request):
    if 'user_id' in request.session:
        return redirect('Board:Home')
    return render(request,'main/index.html')

def auth(request):
    
    email=request.POST['html_email']
    password=request.POST['html_password']
    
    user=User.objects.get(user_email=email)

    if user.user_email == email:
        request.session['user_id']=user.id
        request.session['user_name']=user.user_name
        return redirect('Board:Home')
    else:
        print 'nope'
        return redirect('Main:Home')

def register(request):

    name=request.POST['html_name']
    email=request.POST['html_email']
    password=request.POST['html_password']
    password_confirm=request.POST['html_confirm']
    auth=True

    if len(name)<2:
        auth=False
        messages.add_message(request,messages.ERROR,'Name is too short')
    elif not REGEX.match(email):
        auth=False
        messages.add_message(request,messages.ERROR,'Invalid Email')
    elif len(password)<8:
        auth=False
        messages.add_message(request,messages.ERROR,'password must be at least 8 characters long')
    elif password!=password_confirm:
        auth=False
        messages.add_message(request,messages.ERROR,'Password do not match')
    elif auth == True:
        hashed_password=bcrypt.hashpw(password.encode('UTF-8'),bcrypt.gensalt())
        User.objects.create(user_name=name, user_email=email, user_password=hashed_password)
        request.session['user_id']=User.id
        request.session['user_name']=User.user_name
        return redirect('Board:Home')
    else:
        return redirect('Main:Home')
    

def logout(request):
    request.session.clear()
    return redirect('Main:Home')