
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view , authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Patients , Diagnosis
from .serializer import PatientsSerializers , DiagnosisSerializers



@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_patients(request : Request) :
    
    if not request.user.is_authenticated :
        return Response("Not Allowed", status = status.HTTP_400_BAD_REQUEST)

    request.data["reception"] = request.user.id
    new_patients = PatientsSerializers(data=request.data)
    if new_patients.is_valid():
        new_patients.save()
        return Response({"Patients" : new_patients.data} , status=status.HTTP_200_OK)
    else:
        print(new_patients.errors)
    
    return Response("couldn't create a patients", status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_patients(request: Request):

    if 'search' in request.query_params:
        search_phrase = request.query_params['search']
        patients = Patients.objects.filter(full_name__contains=search_phrase)
    else:
        patients = Patients.objects.order_by('-created_at').all()
        
    responseData = {
       
        "Patients" : PatientsSerializers(instance=patients, many=True).data
    }

    return Response(responseData , status=status.HTTP_200_OK)


@api_view(['PATCH'])
def update_patients(request:Request , patients_id ):
    patient = Patients.objects.get(id=patients_id)

    udate_patient = PatientsSerializers(instance=patient, data=request.data , partial=True)
    if udate_patient.is_valid():
        udate_patient.save()
        responseData = {
            "msg": "updated successefully"
        }

        return Response(responseData , status=status.HTTP_200_OK)
    else:
        print(udate_patient.errors)
        return Response({"msg": "bad request, cannot update"} , status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_patients (request:Request , patients_id ):
    patient = Patients.objects.get(id=patients_id)
    patient.delete()
    return Response({"msg": "Deleted Successfully"} , status=status.HTTP_200_OK)
