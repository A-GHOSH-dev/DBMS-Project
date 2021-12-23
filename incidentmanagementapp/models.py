from django.db import models
import os
#from twilio.rest import Client

# Create your models here.

#adduser
class AddUser(models.Model):
    addemp_id = models.CharField(max_length=50)
    addemail=models.CharField(max_length=50)
    addname=models.CharField(max_length=50)
    addDepartment=models.CharField(max_length=50)
    addsection=models.CharField(max_length=50)
    addrole=models.CharField(max_length=50)
    addtraining=models.CharField(max_length=50)
    addphone=models.CharField(max_length=50)
    addpassword1=models.CharField(max_length=50)

    def __str__(self):
        return self.addemp_id + ' ' + self.addemail + ' ' + self.addname


#IncidentReporting
class IncidentReporting(models.Model):
    datereport=models.CharField(max_length=50)
    timereport=models.CharField(max_length=50)
    dateincident=models.CharField(max_length=50)
    reportedby=models.CharField(max_length=50)
    incident_id=models.CharField(max_length=50)
    timeincident=models.CharField(max_length=50)
    locationincident=models.CharField(max_length=50)
    incidentdesc=models.CharField(max_length=50)
    incidentaction=models.CharField(max_length=50)
    victimname=models.CharField(max_length=50)
    victimrole=models.CharField(max_length=50)
    victimemp_id=models.CharField(max_length=50)
    victimcon_id=models.CharField(max_length=50)

    def __str__(self):
        return self.datereport + ' ' + self.dateincident

#Assignleadinvestigator
class AssignInvestigator(models.Model):
    incident_id=models.CharField(max_length=50)
    nameassignedinvestigator=models.CharField(max_length=50)
    emailassignedinvestigator=models.CharField(max_length=50)

    def __str__(self):
        return self.incident_id + ' ' + self.emailassignedinvestigator

#whywhyanalysis
class WhyWhyAnalyzing(models.Model):
    whyinc_id=models.CharField(max_length=50)
    ps=models.CharField(max_length=500)
    why1=models.CharField(max_length=200)
    why2=models.CharField(max_length=200)
    why3=models.CharField(max_length=200)
    why4=models.CharField(max_length=200)
    why5=models.CharField(max_length=200)
    rc=models.CharField(max_length=500)

    def __str__(self):
        return self.whyinc_id

#specialanalysis
class SpecialAnalyzing(models.Model):
    spe_inc_id=models.CharField(max_length=50)
    imm_cause_unsafe_ac=models.CharField(max_length=500)
    imm_cause_unsafe_con=models.CharField(max_length=500)
    root_cause_human_fac=models.CharField(max_length=500)
    root_cause_org_fac=models.CharField(max_length=500)

    def __str__(self):
        return self.spe_inc_id
#final report
class FinalReport(models.Model):
    #speinc_id=models.CharField(max_length=50)
    reinc_id=models.CharField(max_length=50)
    sum=models.CharField(max_length=500)
    img=models.CharField(max_length=500)
    rca=models.CharField(max_length=500)
    imc=models.CharField(max_length=500)
    rtc=models.CharField(max_length=500)
    ca=models.CharField(max_length=500)   
    cap=models.CharField(max_length=500)
    cad=models.DateField(max_length=500)
    pa=models.CharField(max_length=500)   
    pap=models.CharField(max_length=500)
    pat=models.DateField(max_length=500)
    intensity=models.CharField(max_length=500)

    def __str__(self):
        return self.reinc_id

