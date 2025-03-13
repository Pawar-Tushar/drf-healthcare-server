from rest_framework import serializers
from accounts.models import CustomUser 

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'}) 

    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'password') 

    def create(self, validated_data):
        user = CustomUser.objects.create_user( 
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'] 
        )
        return user