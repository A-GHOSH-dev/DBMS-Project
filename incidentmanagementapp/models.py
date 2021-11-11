from django.db import models
import os
#from twilio.rest import Client

# Create your models here.
#signup
class SignUp(models.Model):
    emp_id = models.CharField(max_length=50)
    email = models.CharField(max_length=50)  
    name = models.CharField(max_length=50)
    Department = models.CharField(max_length=50)
    FactoryNumber = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    
    def __str__(self):
        return self.emp_id + ' ' + self.email + ' ' + self.name


#login
class Login(models.Model):
    loginemp_id = models.CharField(max_length=50)
    loginpassword = models.CharField(max_length=15)  
   
    
    def __str__(self):
        return self.loginemp_id + ' ' + self.loginpassword

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


