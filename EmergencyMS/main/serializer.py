from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Patients , Diagnosis

# to read user
class UserSerializerView(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [ 'id' ,  'username', 'email']

# to read patients
class PatientsSerializerView(serializers.ModelSerializer):

    class Meta:
        model = Patients
        fields = [ 'full_name' ]

class PatientsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Patients
        fields = '__all__'

class DiagnosisSerializers(serializers.ModelSerializer):
  
    class Meta:
        model = Diagnosis
        fields = '__all__'

# to read diagnosis
class DiagnosisSerializersRead(serializers.ModelSerializer):
    patients = PatientsSerializerView()
    nurce = UserSerializerView()
    doctor = UserSerializerView()
    class Meta:
        model = Diagnosis
        fields = '__all__'



