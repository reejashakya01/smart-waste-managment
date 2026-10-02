from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.collector.api.permission import IsCollector
from apps.collector.models import CollectionAssignment
from apps.collector.api.serializers import CollectionAssignmentSerializer

class CollectionRequestView(GenericAPIView):
    queryset = CollectionAssignment.objects.all()
    serializer_class = CollectionAssignmentSerializer
    permission_classes = [IsAuthenticated, IsCollector]  

    def get(self, request):
        assignments = self.get_queryset()
        # assignments = self.get_queryset().filter(collector=request.user)
        serializer = self.get_serializer(assignments, many=True)
        return Response(serializer.data)