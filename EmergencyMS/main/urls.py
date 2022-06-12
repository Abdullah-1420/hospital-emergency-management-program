from django.urls import path
from . import views


urlpatterns = [
    # end point for patient
    path('add_patient' , views.add_patients , name='add_patient'),
    path('all_patients' , views.list_patients , name = 'all_patients'),
    path('update_patient/<patients_id>' , views.update_patients , name = 'update_patient'),
    path('delete_patient/<patients_id>' , views.delete_patients , name = 'delete_patient'),
    # end point for diagnosis
    path('add_diagnosis' , views.add_diagnosis , name='add_diagnosis'),
    path('uncompleted_diagnosis' , views.list_uncompleted_diagnosis , name = 'uncompleted_diagnosis'),
    path('completed_diagnosis' , views.list_completed_diagnosis , name = 'completed_diagnosis'),
    path('update_diagnosis/<diagnosis_id>' , views.add_diagnosis_by_doctor , name = 'update_diagnosis'),
    path('add_user_to_group/<group_name>/<user_id>' , views.add_user_to_group , name = 'add_user_to_group'),
]