from django.shortcuts import render, HttpResponse, redirect
from .models import Member
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return HttpResponse("This is home page")

def home(request):
    return render(request,'../templates/home.html')

def product(request):
    return render(request,'../templates/product.html')

def blog(request):
    return render(request,'../templates/blog.html')

def contact(request):
    return render(request,'../templates/contact.html')

def aboutUs(request):
    return render(request,'../templates/about.html')

def login(request):
    return render(request,'../templates/login.html')

def signUp(request):
    return render(request,'../templates/signup.html')


def register(request):
    if request.method == 'POST':
        _name = request.POST.get('name')
        _email = request.POST.get('email')
        _contact = request.POST.get('contact')
        _address = request.POST.get('address')
        _password = request.POST.get('password')

        new_user = Member(name=_name,email=_email,contact=_contact,address=_address,password=_password)
        new_user.save()
        return render(request, 'home.html')
    else:
        return render(request, 'register.html')

def loginMember(request):
    if request.method == 'POST':
        _email = request.POST['email']
        _password = request.POST['password']
        user = authenticate(request, email=_email, password=_password)
        if user is authenticate:
            login(request, user)
            return render(request, 'home.html')
        else:
            print("hello")
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    else:
        return render(request, 'login.html', {'error_message': 'Invalid method request'})

