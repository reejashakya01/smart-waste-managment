from rest_framework import serializers
from django.db import transaction
import time

from apps.collector.api.services import create_collector_assignment
from apps.waste_collection.api.service import create_collection_activity_log
from apps.waste_collection.models import (
    CollectionActivity,
    CollectionRequest,
    CollectionRequestItem,
)


class CollectionRequestItemSerializer(serializers.ModelSerializer):
    estimated_amount = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        read_only=True
    )

    actual_quantity = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        read_only=True
    )

    reward_points = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        read_only=True
    )

    collection_request = serializers.PrimaryKeyRelatedField(
        read_only=True
    )

    class Meta:
        model = CollectionRequestItem
        fields = "__all__"


class CollectionCompletedItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    estimated_amount = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        read_only=True
    )

    estimated_quantity = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        read_only=True
    )

    actual_quantity = serializers.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    collection_request = serializers.PrimaryKeyRelatedField(
        read_only=True
    )

    class Meta:
        model = CollectionRequestItem
        fields = "__all__"


class UserCollectionRequestSerializer(serializers.ModelSerializer):
    estimated_amount = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        read_only=True
    )

    estimated_weight = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        read_only=True
    )

    priority = serializers.CharField(
        read_only=True
    )

    request_number = serializers.IntegerField(
        read_only=True
    )

    items = CollectionRequestItemSerializer(
        many=True,
        write_only=True
    )

    class Meta:
        model = CollectionRequest
        fields = "__all__"

    def create(self, validated_data):
        items = validated_data.pop("items")

        total_estimated_amount = 0
        total_estimated_weight = 0

        for item in items:
            item["estimated_amount"] = (
                item["waste_category"].base_rate
                * item["estimated_quantity"]
            )

            total_estimated_amount += item["estimated_amount"]
            total_estimated_weight += item["estimated_quantity"]

        validated_data["estimated_amount"] = total_estimated_amount
        validated_data["estimated_weight"] = total_estimated_weight
        validated_data["request_number"] = int(time.time())

        collection_request = super().create(validated_data)

        for item in items:
            item["collection_request"] = collection_request

            collection_item = CollectionRequestItem(**item)
            collection_item.save()

        create_collection_activity_log(
            collection=collection_request,
            message="Requested for collection"
        )

        create_collector_assignment(
            collection=collection_request
        )

        return collection_request

    @transaction.atomic
    def update(self, instance, validated_data):

        if instance.status == CollectionStatus.COMPLETED:
            raise serializers.ValidationError(
                {"items": "Item is already completed"}
            )

        items = validated_data.pop("items")

        total_amount = 0
        total_quantity = 0

        for item in items:
            item_id = item.get("id")

            try:
                collection_item = instance.items.get(id=item_id)

            except CollectionRequestItem.DoesNotExist:
                raise serializers.ValidationError(
                    {
                        "items": f" Item {item_id} does belong to collection request or ID not found"
                    }
                )

            collection_item.actual_quantity = item["actual_quantity"]

            collection_item.actual_amount = (
                item["waste_category"].base_rate
                * item["actual_quantity"]
            )

            collection_item.reward_points = (
                (item["actual_quantity"] // 1)
                * item["waste_category"].reward_points_per_kg
            )

            collection_item.waste_category = item["waste_category"]

            total_amount += float(collection_item.actual_amount)
            total_quantity += float(collection_item.actual_quantity)

            collection_item.save()

        print("--------TA", total_amount)
        print("--------TQ", total_quantity)

        instance.final_amount = total_amount
        instance.final_weight = total_quantity
        instance.status = CollectionStatus.COMPLETED
        instance.save()

        return validated_data