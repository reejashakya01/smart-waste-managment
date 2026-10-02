from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.collector.api.permission import IsCollector, IsAdmin
from rest_framework import status
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
    
class CollectionAssignmentView(GenericAPIView):
    queryset = CollectionAssignment.objects.all()
    serializer_class = CollectionAssignmentSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    def put(self,request, pk):
        collection = self.get_object()
        data = request.data
        serializer = self.serializer_class(collection, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"Collection assigned to collector"
            }, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)