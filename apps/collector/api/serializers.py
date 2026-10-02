from rest_framework import serializers
from apps.collector.models import CollectionAssignment

class CollectionAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionAssignment
        fields = '__all__'