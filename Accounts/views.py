from django.shortcuts import render,redirect
from django.contrib.auth.forms import (
     UserCreationForm,
     AuthenticationForm,
     UserChangeForm,
     PasswordChangeForm
)

from . forms import *
from django.http import HttpResponse
from Stagaire.models import Stagaire
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.contrib.auth.models import Group, User

# Create your views here.

@unauthenticated_user
def signUp(request):
    if request.method =='POST':
        form = registerForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('Accounts:editinfo')
            
        else:
            return render(request,'Accounts/signup.html',{'form':form})
    else:
        form = registerForm()
        dec = {'form':form}
        return render(request,'Accounts/signup.html',dec)
            
@unauthenticated_user
def login_meth(request):
    
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #login user
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/')
        else:
            return render(request,'Accounts/login.html',{'form':form})
    else:
        form = AuthenticationForm()
        return render(request,'Accounts/login.html',{'form':form})


@login_required(login_url="/Accounts/loginUser/")
def editinfo(request):
    if request.method=='POST':
        form = finishInfo(data=request.POST)
        if form.is_valid():
            instance =form.save(commit=False)
            instance.usern = request.user
            
            instance.save()
            g = Group.objects.get(name='users')
            g.user_set.add(instance.usern)

            return redirect('home')
        else:
            return render(request,'Accounts/newStg.html',{'form':form})
    else:
        form = finishInfo()
        return render(request,'Accounts/newStg.html',{'form':form})


@login_required(login_url="/Accounts/loginUser/")
def logOut(request):
    if request.method=='POST':
        logout(request)
        # return render(request,'Master.html')
        return redirect('/')

@allowed_users(allowed_roles=['users'])
@login_required(login_url="/Accounts/loginUser/")
def profile(request):
    args = {'user':request.user}
    return render(request,'Accounts/profile.html',args)

@allowed_users(allowed_roles=['users'])
@login_required(login_url="/Accounts/loginUser/")
def editUser(request):
    if request.method=='POST':
        form = updateUserInfo(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('Accounts:profile')
    else:
        form = updateUserInfo(instance=request.user)
        args = {'form':form}
        return render(request,'Accounts/editUser.html',args)

@allowed_users(allowed_roles=['users']) 
@login_required(login_url="/Accounts/loginUser/")
def changemdp(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST,user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('Accounts:profile')
        else:
            return render(request,'Accounts/editPassword.html',{'form':form})
    else:
        form =  PasswordChangeForm(user=request.user)
        args = {'form':form}
        return render(request,'Accounts/editPassword.html',args)
        