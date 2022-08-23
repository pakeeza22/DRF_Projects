from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Employee, Position

User = get_user_model()


# User Serializer
# class UserSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(required=True, min_length=8, style={'input_type': 'password'})
    password2 = serializers.CharField(required=True, min_length=8, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
                                        validated_data['password1'])
        user.is_staff = True
        return user

    def validate(self, data):
        password1 = data.get('password1')
        password2 = data.get('password2')
        if password1 != password2:
            raise serializers.ValidationError("Passwords doesn't matched!")
        return data


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['emp_name', 'mobile', 'emp_code', 'position']
