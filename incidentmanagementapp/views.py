from django.shortcuts import render, HttpResponse, redirect
from incidentmanagementapp.models import WhyWhyAnalyzing, AddUser, IncidentReporting, AssignInvestigator, SpecialAnalyzing, FinalReport
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

        user=authenticate(username=loginemp_id, password=loginpassword)
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
        messages.success(request, "User has been succesfully added")

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
        messages.success(request, "Incident has been succesfully reported")
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
        messages.success(request, "Lead investigator has been succesfully assigned")
        #return redirect('payment')
        #return render(request,"foodsordernow.html",{"Orders":farmerbuyorder})
        
        
    #return render(request,"foodsordernow.html",{"Orders":adduserdata})
    return render(request,"assignleadinvestigator.html")




def whywhyanalysis(request):
    #return HttpResponse("This is my home page")
    #return render(request, 'whywhyanalysis.html')
    if request.method=="POST":
        whyinc_id=request.POST['whyinc_id']
        ps=request.POST['ps']
        why1=request.POST['why1']
        why2=request.POST['why2']
        why3=request.POST['why3']
        why4=request.POST['why4']
        why5=request.POST['why5']
        rc=request.POST['rc']

        whywhyanalysisdata = WhyWhyAnalyzing(whyinc_id=whyinc_id, ps=ps, why1=why1, why2=why2, why3=why3, why4=why4, why5=why5, rc=rc)  

        whywhyanalysisdata.save()
        messages.success(request, "Why Why Analysis Done")

    
        return redirect('specialanalysis')
        #return redirect('payment')
        #return render(request,"foodsordernow.html",{"Orders":farmerbuyorder})
        
        
    #return render(request,"foodsordernow.html",{"Orders":adduserdata})
    return render(request,"whywhyanalysis.html")

def specialanalysis(request):
    if request.method=="POST":
        spe_inc_id=request.POST['speinc_id']
        imm_cause_unsafe_ac = request.POST['imm_cause_unsafe_ac']
        imm_cause_unsafe_con = request.POST['imm_cause_unsafe_con']
        root_cause_human_fac = request.POST['root_cause_human_fac']
        root_cause_org_fac = request.POST['root_cause_org_fac']

        specialanalysisdata = SpecialAnalyzing(spe_inc_id=spe_inc_id, imm_cause_unsafe_ac=imm_cause_unsafe_ac, imm_cause_unsafe_con=imm_cause_unsafe_con, root_cause_human_fac=root_cause_human_fac, root_cause_org_fac=root_cause_org_fac)  

        specialanalysisdata.save()
        messages.success(request, "Special Analysis Done")

    
        return redirect('finalinvestigationreport')

    return render(request,"specialanalysis.html")
'''
def specialanalysis(request):
    #return HttpResponse("This is my home page")
    #return render(request, 'whywhyanalysis.html')
    if request.method=="POST":
        speinc_id=request.POST['speinc_id']
        speicua = request.POST.getlist('icua[]')
        data_icua=''
        if(len(speicua)>0):
          for data_icua1 in speicua:
            data_icua=data_icua+data_icua1 +" " 
        icuao=request.POST['icuao']
        speicuc = request.POST.getlist('icuc[]')
        data_icuc=''
        if(len(speicua)>0):
          for data_icuc1 in speicua:
            data_icuc=data_icuc+data_icuc1 +" " 
        icuco=request.POST['icuco']
        sperchf = request.POST.getlist('rchf[]')
        data_rchf=''
        if(len(sperchf)>0):
          for data_rchf1 in sperchf:
            data_rchf=data_rchf+data_rchf1 +" "  
        rchfo=request.POST['rchfo'] 
        spercof = request.POST.getlist('rcof[]')
        data_rcof=''
        if(len(spercof)>0):
          for data_rcof1 in spercof:
            data_rcof=data_rcof+data_rcof1 +" " 
        rcofo=request.POST['rcofo']  

        specialanalysisdata = SpecialAnalyzing(speinc_id=speinc_id, speicua=speicua, speicuc=speicuc, sperchf=sperchf, spercof=spercof, icuao=icuao, icuco=icuco, rchfo=rchfo, rcofo=rcofo)  

        specialanalysisdata.save()
        messages.success(request, "Special Analysis Done")

    
        return redirect('finalinvestigationreport')
        #return redirect('payment')
        #return render(request,"foodsordernow.html",{"Orders":farmerbuyorder})
        
        
    #return render(request,"foodsordernow.html",{"Orders":adduserdata})
    return render(request,"specialanalysis.html")

'''
def finalinvestigationreport(request):
    #return HttpResponse("This is my home page")
    #return render(request, 'whywhyanalysis.html')
    if request.method=="POST":
        reinc_id=request.POST['reinc_id']
        sum=request.POST['sum']
        img=request.POST['img']
        rca=request.POST['rca']
        imc=request.POST['imc']
        rtc=request.POST['rtc']
        ca=request.POST['ca']
        cap=request.POST['cap']
        cad=request.POST['cad']
        pa=request.POST['pa']
        pap=request.POST['pap']
        pat=request.POST['pat']
        intensity = request.POST['intensity']

        finalinvestigationreportdata = FinalReport(reinc_id=reinc_id, sum=sum, img=img, rca=rca, imc=imc, rtc=rtc, ca=ca, cap=cap, cad=cad, pa=pa, pap=pap, pat=pat, intensity=intensity)  

        finalinvestigationreportdata.save()
        messages.success(request, "Investigation report succesfully saved")

        #return redirect('payment')
        #return render(request,"foodsordernow.html",{"Orders":farmerbuyorder})
        
        
    #return render(request,"foodsordernow.html",{"Orders":adduserdata})
    return render(request,"finalinvestigationreport.html")