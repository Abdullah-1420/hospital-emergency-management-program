from django.contrib import admin
from .models import Patients, Diagnosis , Prescription

class PAdmin(admin.ModelAdmin):
    '''
     methods for Patients model
    '''
    list_display = ('full_name', 'NationalID','birth_date' , 'phone' , 'created_at')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'
    search_fields = ['NationalID', ]



class DAdmin(admin.ModelAdmin):
    '''
    methods for Diagnosis model
    '''
    list_display = ('patients', 'Temperature','Pressure' , 'sitDescription' , 'drDiagnosis' , 'iscompleted')
    list_filter = ('iscompleted',)
    


class PreAdmin(admin.ModelAdmin):
    '''
    method for Prescription model
    '''
    list_display = ('diagnosis', 'recipe','doctor')



admin.site.register(Patients , PAdmin)
admin.site.register(Diagnosis  , DAdmin)
admin.site.register(Prescription , PreAdmin)
