from django.contrib.auth import authenticate
from django.http import request
from .models import reg ,datas
from django.shortcuts import redirect, render
from django.http import HttpResponse
from calc.models import datas 
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import datas



# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        blood = request.POST.get('blood')
        age   = request.POST.get('age')
        phone = request.POST.get('phone')
        #datas = {'name': name}
        DATA = datas(name=name,blood=blood,age=age,phone=phone)
        DATA.save()
        #return HttpResponse("hi")
    return render(request, 'home.html')


def display(request):
    us = datas.objects.all()
    
    return render(request, 'display.html',{'data': us})





def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        print(username)
        print(password)
        user = authenticate(username=username,password=password)


        if user is not None:
            auth.login(request, user)
            return redirect('display/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('/')
    else:
        return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password   = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password==password2:
            if reg.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('register')
            elif reg.objects.filter(email=email).exists():
                messages.info(request,'email exist')
                return redirect('register')
            else:
                user = reg.objects.create_user(username=username, password=password,email=email)
                user.save();
                print('user created')
                return redirect('login')
        else:
            messages.info(request,'password mismatch')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')        
              
def base(request):
   
    return render(request, 'base.html')






    