from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Specialisation,Doctor,Patient
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    return render(request,'index.html')

# patients

class PatientListView(ListView):
    model = Patient
    template_name = 'patients.html'
    context_object_name = 'patients'
    

class PatientUpdateView(UpdateView):
    model = Patient
    fields = '__all__'
    template_name = 'patientedit.html'
    success_url = reverse_lazy('patient_list')
    

class PatientCreateView(CreateView):
    model = Patient
    fields = '__all__'
    template_name = 'addpatient.html'
    success_url = reverse_lazy('patient_list')


def delete(request, id):
  if request.method == 'POST':
    patient = Patient.objects.get(pk=id)
    patient.delete()
  return HttpResponseRedirect(reverse('patient_list'))

# doctors

class DoctorListView(ListView):
    model = Doctor
    template_name = 'doctors.html'
    context_object_name = 'doctors'
    

class DoctorUpdateView(UpdateView):
    model = Doctor
    fields = '__all__'
    template_name = 'doctoredit.html'
    success_url = reverse_lazy('doctor_list')
    
class DoctorCreateView(CreateView):
    model = Doctor
    fields = '__all__'
    template_name = 'adddoctor.html'
    success_url = reverse_lazy('doctor_list')
    
def doctorDelete(request, id):
  if request.method == 'POST':
    doctor = doctor.objects.get(pk=id)
    doctor.delete()
  return HttpResponseRedirect(reverse('doctor_list'))
    
# departments

class DepartmentListView(ListView):
    model = Specialisation
    template_name = 'departments.html'
    context_object_name = 'departments'


class DepartmentUpdateView(UpdateView):
    model = Specialisation
    fields = '__all__'
    template_name = 'depedit.html'
    success_url = reverse_lazy('department_list')


class DepartmentCreateView(CreateView):
    model = Specialisation
    fields = '__all__'
    template_name = 'adddep.html'
    success_url = reverse_lazy('department_list')


def depdelete(request, id):
  if request.method == 'POST':
    department = Specialisation.objects.get(pk=id)
    department.delete()
  return HttpResponseRedirect(reverse('department_list'))