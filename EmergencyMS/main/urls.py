from django.urls import path
from . import views


urlpatterns = [

    path('add_patient' , views.add_patients , name='add_patient'),
    path('all_patients' , views.list_patients , name = 'all_patients'),
    path('update_patient/<patients_id>' , views.update_patients , name = 'update_patient'),
    path('delete_patient/<patients_id>' , views.delete_patients , name = 'delete_patient'),
]