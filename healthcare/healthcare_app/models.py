from django.db import models
from accounts.models import CustomUser  

class Patient(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20) 
    contact_number = models.CharField(max_length=20, blank=True, null=True) 
    address = models.TextField(blank=True, null=True)
    medical_history = models.TextField(null=True, blank=True)  
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255, blank=True, null=True) 
    department = models.CharField(max_length=255, blank=True, null=True) 
    license_number = models.CharField(max_length=255, blank=True, null=True)      
    contact_number = models.CharField(max_length=20, blank=True, null=True)  
    email = models.EmailField(blank=True, null=True)                          
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " (" + self.specialization + ")" if self.specialization else self.name 
    


class PatientDoctorMapping(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="doctor_mappings")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="patient_mappings")
    assigned_on = models.DateTimeField(auto_now_add=True) 
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)     

    def __str__(self):
        return f"{self.patient.name} assigned to {self.doctor.name}"

    class Meta:
        unique_together = ('patient', 'doctor')
        verbose_name = 'Patient-Doctor Mapping'
        verbose_name_plural = 'Patient-Doctor Mappings'