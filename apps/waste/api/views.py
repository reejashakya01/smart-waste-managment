
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from apps.waste.models import WasteCategory
from apps.waste.api.serializers import WasteCategorySerializer


class WasteCategoryView(GenericAPIView):
    queryset = WasteCategory
    serializer_class = WasteCategorySerializer

    def get(self,request):
        data = WasteCategory.objects.all()
        serializer = WasteCategorySerializer(data, many=True)
        return Response(serializer.data,status.HTTP_200_OK)