from django.shortcuts import render, HttpResponse, redirect
#from incidentmanagementapp.models import SignUp, Login, AddUser, IncidentReporting, AssignInvestigator, CustomerOrder
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def index(request):
    #return HttpResponse("This is my home page")
    return render(request, 'index.html')
def allincidentslist(request):
    #return HttpResponse("This is my home page")
    return render(request, 'allincidentslist.html')

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
        emp_id=request.POST['emp_id']
        email=request.POST['email']
        name=request.POST['name']  
        Department=request.POST['Department']
        FactoryNumber=request.POST['FactoryNumber']
        phone=request.POST['phone']
        password1=request.POST['password1']
        password2=request.POST['password2']

        myuser = User.objects.create_user(emp_id, email, password1)
        myuser.person_name=name
        myuser.save()
        messages.success(request, "Your account has been successfully created")

    
        return redirect('/')


def handleLogin(request):
    if request.method=='GET':
        return render(request, 'login.html')
        
    if request.method=='POST':
        loginemp_id=request.POST['loginemp_id'] 
        loginpassword=request.POST['loginpassword']

        user=authenticate(emp_id=loginemp_id, password1=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect('index')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('handleLogin')
    


def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('/')



def adduser(request):
    #return HttpResponse("This is my home page")
    #return render(request, 'adduser.html')
    if request.method=="POST":
        addemp_id=request.POST['addemp_id']
        addemail=request.POST['addemail']
        addname=request.POST['addname']
        addDepartment=request.POST['addDepartment']
        addsection=request.POST['addsection']
        addrole=request.POST['addrole']
        addtraining=request.POST['addemp_id']
        addphone=request.POST['addphone']
        addpassword1=request.POST['addpassword1']

        adduserdata = AddUser(addemp_id=addemp_id, addemail=addemail, addname=addname, addDepartment=addDepartment, addsection=addsection, addrole=addrole, addtraining=addtraining, addphone=addphone, addpassword1=addpassword1)  

        adduserdata.save()
        #return redirect('payment')
        #return render(request,"foodsordernow.html",{"Orders":farmerbuyorder})
        
        
    #return render(request,"foodsordernow.html",{"Orders":adduserdata})
    return render(request,"adduser.html")





def incidentreport(request):
    #return HttpResponse("This is my home page")
    #return render(request, 'incidentreport.html')
    if request.method=="POST":
        datereport=request.POST['datereport']
        timereport=request.POST['timereport']
        reportedby=request.POST['reportedby']
        dateincident=request.POST['dateincident']
        timeincident=request.POST['timeincident']
        locationincident=request.POST['locationincident']
        incidentdesc=request.POST['incidentdesc']
        incidentaction=request.POST['incidentaction']
        victimname=request.POST['victimname']
        victimrole=request.POST['victimrole']
        victimemp_id=request.POST['victimemp_id']
        victimcon_id=request.POST['victimcon_id']

        incidentreportingdata = IncidentReporting(datereport=datereport, timereport=timereport, reportedby=reportedby, dateincident=dateincident, timeincident=timeincident, locationincident=locationincident, incidentdesc=incidentdesc, incidentaction=incidentaction, victimname=victimname, victimrole=victimrole, victimemp_id=victimemp_id, victimcon_id=victimcon_id)  

        incidentreportingdata.save()
        #return redirect('payment')
        #return render(request,"foodsordernow.html",{"Orders":farmerbuyorder})
        
        
    #return render(request,"foodsordernow.html",{"Orders":adduserdata})
    return render(request,"incidentreport.html")



def assignleadinvestigator(request):
    #return HttpResponse("This is my home page")
    #return render(request, 'assignleadinvestigator.html')
    if request.method=="POST":
        incident_id=request.POST['incident_id']
        nameassignedinvestigator=request.POST['nameassignedinvestigator']
        emailassignedinvestigator=request.POST['emailassignedinvestigator']

        assignleadinvestigatorreport = AssignInvestigator(incident_id=incident_id, nameassignedinvestigator=nameassignedinvestigator, emailassignedinvestigator=emailassignedinvestigator)  

        assignleadinvestigatorreport.save()
        #return redirect('payment')
        #return render(request,"foodsordernow.html",{"Orders":farmerbuyorder})
        
        
    #return render(request,"foodsordernow.html",{"Orders":adduserdata})
    return render(request,"assignleadinvestigator.html")




def whywhyanalysis(request):
    #return HttpResponse("This is my home page")
    #return render(request, 'whywhyanalysis.html')
    if request.method=="POST":
        datereport=request.POST['datereport']
        timereport=request.POST['timereport']
        reportedby=request.POST['reportedby']
        dateincident=request.POST['dateincident']
        timeincident=request.POST['timeincident']
        locationincident=request.POST['locationincident']
        incidentdesc=request.POST['incidentdesc']
        incidentaction=request.POST['incidentaction']
        victimname=request.POST['victimname']
        victimrole=request.POST['victimrole']
        victimemp_id=request.POST['victimemp_id']
        victimcon_id=request.POST['victimcon_id']

        incidentreportingdata = IncidentReporting(datereport=datereport, timereport=timereport, reportedby=reportedby, dateincident=dateincident, timeincident=timeincident, locationincident=locationincident, incidentdesc=incidentdesc, incidentaction=incidentaction, victimname=victimname, victimrole=victimrole, victimemp_id=victimemp_id, victimcon_id=victimcon_id)  

        incidentreportingdata.save()
        #return redirect('payment')
        #return render(request,"foodsordernow.html",{"Orders":farmerbuyorder})
        
        
    #return render(request,"foodsordernow.html",{"Orders":adduserdata})
    return render(request,"whywhyanalysis.html")

