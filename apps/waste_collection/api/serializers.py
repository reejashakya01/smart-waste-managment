
from rest_framework import serializers
from apps.waste_collection.models import CollectionActivity, CollectionRequest, CollectionRequestItem


class UserCollectionRequestSerializer(serializers.ModelSerializer):
    estimated_amount = serializers.DecimalField(max_digits=10, decimal_places=2,read_only=True)
    priority = serializers.CharField(read_only=True)

    class Meta:
        model = CollectionRequest
        fields = '__all__'

    def create(self, validated_data):
        validated_data['estimated_amount'] = 200
        return super().create(validated_data)