
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# taple for patients
class Patients (models.Model):
     reception = models.ForeignKey(User , on_delete=models.DO_NOTHING)
     created_at= models.DateTimeField(auto_now_add=True)
     full_name = models.CharField(max_length=128)
     NationalID = models.CharField(max_length=64)
     birth_date = models.DateField()
     phone = models.CharField(max_length=32)

     def __str__(self) :
          return self.full_name
     
   


# taple for diagnosis
class Diagnosis(models.Model):
    patients = models.ForeignKey(Patients , on_delete=models.DO_NOTHING)
    nurce = models.ForeignKey(User , on_delete=models.DO_NOTHING)
    Temperature = models.DecimalField(max_digits=3 , decimal_places=1)
    Pressure = models.CharField(max_length=32)
    sitDescription = models.TextField()
    doctor = models.ForeignKey(User , on_delete=models.DO_NOTHING , related_name='doctor')
    drDiagnosis = models.TextField(blank=True)
    iscompleted = models.BooleanField(default=False , blank=True)
    
    def __str__(self) :
         return self.patients






