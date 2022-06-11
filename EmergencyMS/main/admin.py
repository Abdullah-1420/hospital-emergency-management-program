from django.contrib import admin
from .models import Patients, Diagnosis


admin.site.register(Patients)
admin.site.register(Diagnosis)
