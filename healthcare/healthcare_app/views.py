from rest_framework import viewsets, permissions, generics, decorators
from .models import Patient
from .models import Doctor , PatientDoctorMapping
from .serializers import PatientSerializer , PatientDoctorMappingSerializer 
from .serializers import DoctorSerializer
from rest_framework.response import Response
from rest_framework import status


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all() 
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated] 

    def get_queryset(self):
        user = self.request.user
        return Patient.objects.filter(created_by=user)

    def perform_create(self, serializer):
        print("perform_create method is being called!")
        serializer.save(created_by=self.request.user)


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return Doctor.objects.filter(created_by=user)
    
    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)





class PatientDoctorMappingViewSet(viewsets.ModelViewSet):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated] 
    
    @decorators.action(detail=False, methods=['get'], url_path=r'patient/(?P<patient_pk>\d+)') 
    def patient_doctors(self, request, patient_pk=None):
        try:
            patient = Patient.objects.get(pk=patient_pk) 
        except Patient.DoesNotExist:
            return Response({"error": "Patient not found."}, status=status.HTTP_404_NOT_FOUND)

        mappings = PatientDoctorMapping.objects.filter(patient=patient) 
        serializer = PatientDoctorMappingSerializer(mappings, many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK) 

    def destroy(self, request, pk=None):
        return super().destroy(request, pk) 