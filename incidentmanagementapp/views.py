from django.shortcuts import render

#from incientmanagementsoftware.settings import RAZORPAY_API_KEY
from django.shortcuts import render, HttpResponse, redirect
#from KrishiSahayak.models import SignUp, Login, FoodOrder, ShopUpload, FarmerUpload, CustomerOrder
#import razorpay
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def index(request):
    #return HttpResponse("This is my home page")
    return render(request, 'index.html')
def adduser(request):
    #return HttpResponse("This is my home page")
    return render(request, 'adduser.html')
def incidentreport(request):
    #return HttpResponse("This is my home page")
    return render(request, 'incidentreport.html')
def assignleadinvestigator(request):
    #return HttpResponse("This is my home page")
    return render(request, 'assignleadinvestigator.html')
def allincidentslist(request):
    #return HttpResponse("This is my home page")
    return render(request, 'allincidentslist.html')
def whywhyanalysis(request):
    #return HttpResponse("This is my home page")
    return render(request, 'whywhyanalysis.html')
def specialanalysis(request):
    #return HttpResponse("This is my home page")
    return render(request, 'specialanalysis.html')
def investigationreport(request):
    #return HttpResponse("This is my home page")
    return render(request, 'investigationreport.html') 
def finalinvestigationreport(request):
    #return HttpResponse("This is my home page")
    return render(request, 'finalinvestigationreport.html') 
def actionclosure(request):
    #return HttpResponse("This is my home page")
    return render(request, 'actionclosure.html') 
def verifyactionclose(request):
    #return HttpResponse("This is my home page")
    return render(request, 'verifyactionclose.html') 
def incidentenquiry(request):
    #return HttpResponse("This is my home page")
    return render(request, 'incidentenquiry.html') 


def handleSignup(request):
    if request.method=='GET':
        return render(request, 'signup.html')
    if request.method=='POST':
        #Get parameters posted
        username=request.POST['username']
        email=request.POST['email']
        Sfirstname=request.POST['Sfirstname']
        Slastname=request.POST['Slastname']        
        Department=request.POST['Department']
        FactoryNumber=request.POST['FactoryNumber']
        Scity=request.POST['Scity']
        Saddress=request.POST['Saddress']
        Spin=request.POST['Spin']
        Sphone=request.POST['Sphone']
        pass1=request.POST['pass1']
        pass2=request.POST['pass1']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name=Sfirstname
        myuser.Last_name=Slastname
        myuser.save()
        messages.success(request, "Your account has been successfully created")

    
        return redirect('/')


def handleLogin(request):
    if request.method=='GET':
        return render(request, 'login.html')
        
    if request.method=='POST':
        loginusername=request.POST['loginusername'] 
        loginpassword=request.POST['loginpassword']

        user=authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('handleLogin')
    


def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('/')
