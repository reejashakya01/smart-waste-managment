from rest_framework import serializers
from apps.collector.models import CollectionAssignment
import os
from rest_framework.validators import ValidationError

class CollectionAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionAssignment
        fields = '__all__'
        
        
    def validate_collector(self,collector):
        collector_limit = os.getenv('COLLECTOR_TASK_LIMIT')
        collection_assignment = CollectionAssignment.objects.filter(
            collector = collector
        ).count()
        if collection_assignment >= collector_limit:
            raise ValidationError("Collector reached task limit")
        return collector  