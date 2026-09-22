from rest_framework import serializers
from apps.accounts.models import User
from rest_framework.validators import ValidationError


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField()
    class Meta:
        model = User
        fields = ['username','password','first_name','last_name','email','phone_number']
        fields = ['username','password','first_name','last_name','email','phone_number','confirm_password']


    def validate(self, attrs):
        if attrs['password']!=attrs['confirm_password']:
            raise ValidationError("Password and confirm password doesnot match")
        return super().validate(attrs)

    def validate_phone_number(self, phone_number):
        if phone_number !=10:
            raise ValidationError("Length of phone number should be 10")
        return phone_number

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        return super().create(validated_data)