from rest_framework import serializers
from .models import Patient
from .models import Doctor , PatientDoctorMapping

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name', 'date_of_birth', 'gender', 'contact_number', 'address','medical_history', 'created_at', 'updated_at'] 



class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialization', 'department','license_number', 'contact_number', 'email','created_at', 'updated_at'] 




class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDoctorMapping
        fields = '__all__' 

    def validate(self, data):
        patient = data.get('patient')
        doctor = data.get('doctor')

        if PatientDoctorMapping.objects.filter(patient=patient, doctor=doctor).exists():
            raise serializers.ValidationError("This doctor is already assigned to this patient.")
        return data
    

