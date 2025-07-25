from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.PositiveIntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    CONSULT_TYPES = [
        ('online', 'Online'),
        ('in-person', 'In-Person')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add this line
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    consult_type = models.CharField(max_length=20, choices=CONSULT_TYPES)
    date = models.DateField()
    time = models.TimeField()
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient_name} - {self.doctor.name} - {self.date}"
