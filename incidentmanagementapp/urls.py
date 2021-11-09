from django.contrib import admin
from django.urls import path, include
from incidentmanagementapp import views

admin.site.site_header ="Developer Ananya Ghosh"
admin.site.site_title= "Welcome to my dashboard"
admin.site.index_title="Welcome to my portal"

urlpatterns = [
    
    path('', views.index, name='index'),
    #path('home', views.home, name='home'),
   # path('signup', views.signup, name='signup'),
    path('signup', views.handleSignup, name='handleSignup'),
    path('login', views.handleLogin, name='handleLogin'),
    path('logout', views.handleLogout, name='handleLogout'),
    path('adduser', views.adduser, name='adduser'),
    path('incidentreport', views.incidentreport, name='incidentreport'),
    path('assignleadinvestigator', views.assignleadinvestigator, name='assignleadinvestigator'),
    path('allincidentslist', views.allincidentslist, name='allincidentslist'),
    path('whywhyanalysis', views.whywhyanalysis, name='whywhyanalysis'),
    path('specialanalysis', views.specialanalysis, name='specialanalysis'),
    path('investigationreport', views.investigationreport, name='investigationreport'),
    path('finalinvestigationreport', views.finalinvestigationreport, name='finalinvestigationreport'),
    path('actionclosure', views.actionclosure, name='actionclosure'),
    path('verifyactionclose', views.verifyactionclose, name='verifyactionclose'),
    path('incidentenquiry', views.incidentenquiry, name='incidentenquiry'),
    #path('payment', views.payment, name='payment')




    


    
]

