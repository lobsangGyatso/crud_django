from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from .models import Contact,User
from django.contrib import messages
from .forms import StudentRegistration
# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request, 'about.html')
def services(request):
    return render(request,'services.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'successfully added')
    return render(request,'contact.html')
def detail(request):
    user = {
        'name' : 'lobsang',
        'age' : 24
    }
    return render(request,'detail.html',{'user':user})
# def login(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
        
#         user = authenticate(username=username,password=password)
#         if user is not None:
#             return redirect('/')
#         else:
#             return render(request, 'login.html')
#     else:
#         return render(request,'login.html')
def add_show(request):
    stud = User.objects.all()
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            reg= User(name=name,email=email,password=password)
            reg.save()

    else:
        fm = StudentRegistration(request.POST)
    return render(request,'addandhsow.html',{'form':fm,'std':stud})

# htis function will update/edit
def update_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk = id )
        fm = StudentRegistration(request.POST,instance = pi)
        if fm.is_valid():
            print("we are the one")
            fm.save()
            return redirect('/')
        else:
            print("sdfs")
    else:
        pi = User.objects.get(pk = id )
        fm = StudentRegistration(instance = pi)
    return render(request,'update.html',{'form':fm})

# this functin will delete 
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return redirect('/')