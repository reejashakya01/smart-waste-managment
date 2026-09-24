from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from apps.waste.models import WasteCategory
from apps.waste.api.serializers import WasteCategorySerializer
from django.shortcuts import get_object_or_404


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
            return Response(
                {
                    "message": "Waste Category added successfully",
                    "data": serializer.data,
                },
                status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class WasteUpdateDetailDeleteView(GenericAPIView):
    queryset = WasteCategory.objects.all()
    serializer_class = WasteCategorySerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        # data = get_object_or_404(WasteCategory, id=pk)
                    # or
        data = self.get_object()
        serializer = self.get_serializer(data)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, pk):
        waste_category = get_object_or_404(WasteCategory, id=pk)
        serializer = self.get_serializer(waste_category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Waste Category updated successfully",
                    "data": serializer.data,
                },
                status.HTTP_200_OK,
            )
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk):
        waste_category = get_object_or_404(WasteCategory, id=pk)
        waste_category.delete()
        return Response({
            "message":"Waste Category deleted successfully"
        }, status.HTTP_200_OK)

class WasteCategoryCreateView(GenericAPIView):
    queryset = WasteCategory.objects.all()
    serializer_class = WasteCategorySerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    "message": "Waste Category created successfully",
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class WasteCategoryDeleteView(GenericAPIView):
    queryset = WasteCategory.objects.all()

    def delete(self, request, pk):
        waste_category = get_object_or_404(
            WasteCategory,
            id=pk
        )

        waste_category.delete()

        return Response(
            {
                "message": "Waste Category deleted successfully"
            },
            status=status.HTTP_200_OK,
        )