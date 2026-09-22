from rest_framework import serializers
from apps.address.models import UserAddress
from rest_framework.validators import ValidationError
from rest_framework.exceptions import PermissionDenied


class AddressSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    longitude = serializers.CharField(read_only=True)
    class Meta:
        model = UserAddress
        fields = '__all__'


    def validate_user(self, user):
        request = self.context
        if request.user.id != user.id:
            # raise ValidationError("Login user and request user are different")
            raise PermissionDenied("Login user and request user are different")
        return user
    
def create(self, validated_data):
        validated_data['user']= self.context.user
        return super().create(validated_data)