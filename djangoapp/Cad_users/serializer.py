from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'password', 'first_name', 'last_name',
            'phone', 'cpf', 'address', 'state', 'city', 'zip_code'
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
        }
    
    def create(self, validated_data):
        # Criptografa a senha antes de salvar
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)
