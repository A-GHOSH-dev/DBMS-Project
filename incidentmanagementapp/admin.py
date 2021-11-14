from django.contrib import admin
from incidentmanagementapp.models import WhyWhyAnalyzing, AddUser, IncidentReporting, AssignInvestigator, SpecialAnalyzing, FinalReport

# Register your models here.
admin.site.register(WhyWhyAnalyzing)
admin.site.register(AddUser)
admin.site.register(IncidentReporting)
admin.site.register(AssignInvestigator)
admin.site.register(SpecialAnalyzing)
admin.site.register(FinalReport)
