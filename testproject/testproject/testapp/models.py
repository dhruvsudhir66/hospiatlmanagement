from django.db import models


class Specialisation(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

gender = (
    ('Male','Male'),
    ('Female','Female')
)

class Doctor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10,choices=gender)
    specialisation = models.ForeignKey(Specialisation,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Patient(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10,choices=gender)
    diagnosis = models.CharField(max_length=255)
    doctor_assigned = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    diagnosed_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    