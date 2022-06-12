
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view , authentication_classes , permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Patients , Diagnosis
from .serializer import PatientsSerializers , DiagnosisSerializers , DiagnosisSerializersRead
from django.contrib.auth.models import User


# to add new patients
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_patients(request : Request) :
    
    if not request.user.is_authenticated or not request.user.has_perm('main.add_patients'):
        return Response("Not Allowed", status = status.HTTP_400_BAD_REQUEST)

    request.data["reception"] = request.user.id
    new_patients = PatientsSerializers(data=request.data)
    if new_patients.is_valid():
        new_patients.save()
        return Response({"Patients" : new_patients.data} , status=status.HTTP_200_OK)
    else:
        print(new_patients.errors)
    
    return Response("couldn't create a patients", status = status.HTTP_400_BAD_REQUEST)

# to list all patients 
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list_patients(request: Request):

    if not request.user.is_authenticated or not request.user.has_perm('main.view_patients'):
        return Response("Not Allowed", status = status.HTTP_400_BAD_REQUEST)


    if 'search' in request.query_params:
        search_phrase = request.query_params['search']
        patients = Patients.objects.filter(full_name__contains=search_phrase)
    else:
        patients = Patients.objects.order_by('-created_at').all()
        
    responseData = {
       
        "Patients" : PatientsSerializers(instance=patients, many=True).data
    }

    return Response(responseData , status=status.HTTP_200_OK)

# to update patients
@api_view(['PATCH'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_patients(request:Request , patients_id ):

    if not request.user.is_authenticated or not request.user.has_perm('main.change_patients'):
        return Response("Not Allowed", status = status.HTTP_400_BAD_REQUEST)


    patient = Patients.objects.get(id=patients_id)

    update_patient = PatientsSerializers(instance=patient, data=request.data , partial=True)
    if update_patient.is_valid():
        update_patient.save()
        responseData = {
            "msg": "updated successefully"
        }

        return Response(responseData , status=status.HTTP_200_OK)
    else:
        print(update_patient.errors)
        return Response({"msg": "bad request, cannot update"} , status=status.HTTP_400_BAD_REQUEST)

# to delete patients
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_patients (request:Request , patients_id ):

    if not request.user.is_authenticated or not request.user.has_perm('main.delete_patients'):
        return Response("Not Allowed", status = status.HTTP_400_BAD_REQUEST)

    try:
        patient = Patients.objects.get(id=patients_id)
        patient.delete()
        return Response({"msg": "Deleted Successfully"} , status=status.HTTP_200_OK)
    except:
        return Response({"msg": "Patient not found"} , status=status.HTTP_404_NOT_FOUND)


# to add new diagnosis
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_diagnosis(request : Request) :
    
    if not request.user.is_authenticated or not request.user.has_perm('main.add_diagnosis'):
        return Response("Not Allowed", status = status.HTTP_400_BAD_REQUEST)

    doctor_id = request.data.get("doctor")
    if not User.objects.get(id=doctor_id).groups.filter(name='doctors').exists():
        return Response(" NOT found" , status=status.HTTP_404_NOT_FOUND)   

    request.data["nurce"] = request.user.id
    new_diagnosis = DiagnosisSerializers(data=request.data)
    if new_diagnosis.is_valid():
        new_diagnosis.save()
        return Response({"Diagnosis" : new_diagnosis.data} , status=status.HTTP_200_OK)
    else:
        print(new_diagnosis.errors)
        
    return Response("couldn't create a diagnosis", status = status.HTTP_400_BAD_REQUEST)

# to list all uncompleted iagnosis
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list_uncompleted_diagnosis(request: Request):

    if not request.user.is_authenticated or not request.user.has_perm('main.view_diagnosis'):
        return Response("Not Allowed", status = status.HTTP_400_BAD_REQUEST)

    if 'search' in request.query_params:
        search_phrase = request.query_params['search']
        diagnosis = Diagnosis.objects.filter(patients=search_phrase)
    else:
        diagnosis = Diagnosis.objects.filter(iscompleted=False)
        
    responseData = {
       
        "Diagnosis" : DiagnosisSerializersRead(instance=diagnosis, many=True).data
    }

    return Response(responseData , status=status.HTTP_200_OK)

# to list all completed iagnosis
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list_completed_diagnosis(request: Request):
    if not request.user.is_authenticated or not request.user.has_perm('main.view_diagnosis'):
        return Response("Not Allowed", status = status.HTTP_400_BAD_REQUEST)


    if 'search' in request.query_params:
        search_phrase = request.query_params['search']
        diagnosis = Diagnosis.objects.filter(patients=search_phrase)
    else:
        diagnosis = Diagnosis.objects.filter(iscompleted=True)
        
    responseData = {
       
        "Diagnosis" : DiagnosisSerializersRead(instance=diagnosis, many=True).data
    }

    return Response(responseData , status=status.HTTP_200_OK)


# to complete the diagnosis by doctor
@api_view(['PATCH'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_diagnosis_by_doctor(request:Request , diagnosis_id ):

    if not request.user.is_authenticated or not request.user.has_perm('main.change_diagnosis'):
        return Response("Not Allowed", status = status.HTTP_400_BAD_REQUEST)


    diagnosis = Diagnosis.objects.get(id=diagnosis_id)

    update_diagnosis = DiagnosisSerializers(instance=diagnosis, data=request.data , partial=True)
    if update_diagnosis.is_valid():
        update_diagnosis.save()
        responseData = {
            "msg": "updated successefully"
        }

        return Response(responseData , status=status.HTTP_200_OK)
    else:
        print(update_diagnosis.errors)
        return Response({"msg": "bad request, cannot update"} , status=status.HTTP_400_BAD_REQUEST)



