from django.core.checks import messages
from django.shortcuts import render,redirect
from home.models import Contact
from datetime import datetime
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.htm')
    # return HttpResponse("hey! I am nikhil")

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        user = authenticate(password=password, email=email, firstname=firstname, lastname=lastname)
        if user is not None:
            login(request, user)
            print('user created')
            return render(request, 'index1.htm')
        else:
            return render(request, 'register.htm')
    else:
        return render(request,'register.htm')


def services(request):
    return render(request,'services.htm')
    # return HttpResponse("This is services page")

def contact(request):
    return render(request,'contact.htm')

def form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email,phone=phone,desc=desc,date=datetime.today())
        messages.success(request,"Your message have been sent!")
    
    return render(request,'contact.htm')


    # return HttpResponse("This is contact page")