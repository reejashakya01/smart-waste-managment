from rest_framework import serializers
from apps.waste_collection.models import (
    CollectionActivity,
    CollectionRequest,
    CollectionRequestItem,
)
import time

class CollectionRequestItemSerializer(serializers.ModelSerializer):
    estimated_amount = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )
    actual_quantity = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )
    reward_points = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )

    collection_request = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = CollectionRequestItem
        fields = "__all__"


class UserCollectionRequestSerializer(serializers.ModelSerializer):
    estimated_amount = serializers.DecimalField(max_digits=10, decimal_places=2,read_only=True)
    estimated_amount = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )
    estimated_weight = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )
    priority = serializers.CharField(read_only=True)
    request_number = serializers.IntegerField(read_only=True)
    items = CollectionRequestItemSerializer(many=True, write_only=True)

    class Meta:
        model = CollectionRequest
        fields = '__all__'
        fields = "__all__"

    def create(self, validated_data):
        validated_data['estimated_amount'] = 200
        return super().create(validated_data)
        items = validated_data.pop('items')
        total_estimated_amount = 0
        total_estimated_weight = 0
        for item in items:
            item['estimated_amount'] = item['waste_category'].base_rate * item['estimated_quantity']
            total_estimated_amount +=item['estimated_amount']
            total_estimated_weight +=item['estimated_quantity']

        validated_data['estimated_amount'] = total_estimated_amount
        validated_data['estimated_weight'] = total_estimated_weight
        validated_data['request_number'] =  int(time.time())


        collection_request = super().create(validated_data)
        for item in items:
            item['collection_request'] = collection_request
            collection_item = CollectionRequestItem(**item)
            collection_item.save()

        return validated_data