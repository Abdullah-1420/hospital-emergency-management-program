from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Patients , Diagnosis , Prescription


class UserSerializerView(serializers.ModelSerializer):
    '''
    # to read user
    '''

    class Meta:
        model = User
        fields = [ 'id' ,  'username', 'email']


class PatientsSerializerView(serializers.ModelSerializer):
    '''
    # to read patients
    '''
    class Meta:
        model = Patients
        fields = [ 'full_name' ]


class DiagnosisSerializerView(serializers.ModelSerializer):
    '''
    # to read Diagnosis
    '''
    patients = PatientsSerializerView()
    class Meta:
        model = Diagnosis
        fields = [ "id" , 'patients' ]




class PatientsSerializers(serializers.ModelSerializer):
    '''
    # Serializers for patients model
    '''

    class Meta:
        model = Patients
        fields = '__all__'



class DiagnosisSerializers(serializers.ModelSerializer):
    '''
    # Serializers for diagnosis model
    '''
  
    class Meta:
        model = Diagnosis
        fields = '__all__'


class PrescriptionSerializers(serializers.ModelSerializer):
    '''
    # Serializers for prescription model
    '''
  
    class Meta:
        model = Prescription
        fields = '__all__'

class PrescriptionSerializersView(serializers.ModelSerializer):
    '''
    # to read  prescription
    '''
    diagnosis = DiagnosisSerializerView()
    doctor = UserSerializerView()
    class Meta:
        model = Prescription
        fields = '__all__'


class DiagnosisSerializersRead(serializers.ModelSerializer):
    '''
    # to read diagnosis
    '''
    patients = PatientsSerializerView()
    nurce = UserSerializerView()
    doctor = UserSerializerView()
    class Meta:
        model = Diagnosis
        fields = '__all__'



