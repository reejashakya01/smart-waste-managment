
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from apps.waste.models import WasteCategory
from apps.waste.api.serializers import WasteCategorySerializer


class WasteCategoryView(GenericAPIView):
    queryset = WasteCategory.objects.all()
    serializer_class = WasteCategorySerializer

    def get(self,request):
        data = self.get_queryset()
        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data,status.HTTP_200_OK)
    
    def post(self, request):   
        data = request.data  
        serializer = self.get_serializer(data=data) 
        if serializer.is_valid():           
            serializer.save()           
            return Response({ "message":"Waste Category added successfully",
                             "data":serializer.data }, 
                            status.HTTP_201_CREATED)   
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
