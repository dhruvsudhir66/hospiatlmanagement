from django.urls import path
from . import views
from .views import PatientListView,PatientUpdateView,DoctorListView,DoctorUpdateView,DepartmentListView,PatientCreateView,DoctorCreateView,DepartmentCreateView,DepartmentUpdateView

urlpatterns = [
    path('',views.index,name='index'),
    path('patient',PatientListView.as_view(),name='patient_list'),
    path('update/<int:pk>/',PatientUpdateView.as_view(),name='patient_update'),
    path('create',PatientCreateView.as_view(),name='patient_create'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('doctor',DoctorListView.as_view(),name='doctor_list'),
    path('docedit/<int:pk>/',DoctorUpdateView.as_view(),name='doctor_update'),
    path('doccreate',DoctorCreateView.as_view(),name='doctor_create'),
    path('docdelete/<int:id>/', views.doctorDelete, name='doc_delete'),
    path('department',DepartmentListView.as_view(),name='department_list'),
    path('depedit/<int:pk>/',DepartmentUpdateView.as_view(),name='dep_update'),
    path('depcreate',DepartmentCreateView.as_view(),name='dep_create'),
    path('depdelete/<int:id>/', views.depdelete, name='depdelete'),
]