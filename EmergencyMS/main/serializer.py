from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Patients , Diagnosis



class PatientsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Patients
        fields = '__all__'

class DiagnosisSerializers(serializers.ModelSerializer):

    class Meta:
        model = Diagnosis
        fields = '__all__'



