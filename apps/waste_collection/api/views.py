from rest_framework.generics import GenericAPIView
from apps.waste_collection.models import CollectionRequest
from apps.waste_collection.api.serializers import UserCollectionRequestSerializer

from rest_framework.permissions import IsAuthenticated
from apps.waste_collection.api.permission import IsCustomerOrAdmin
from rest_framework.response import Response

class UserCollectionRequestView(GenericAPIView):
    queryset = CollectionRequest
    serializer_class = UserCollectionRequestSerializer
    permission_classes = [IsAuthenticated, IsCustomerOrAdmin]


    def get(self, request,):
        waste_collection = CollectionRequest.objects.all()
        serializer = self.get_serializer(waste_collection, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Collection  updated successfully"},
                status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)