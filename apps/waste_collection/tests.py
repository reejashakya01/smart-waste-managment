from django.db.migrations import serializer
from django.test import TestCase
from apps import waste_collection
from apps.waste_collection.api.permission import IsCustomerOrAdmin
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from rest_framework.generics import GenericAPIView

# Create your tests here.
class UserCollectionRequestView(GenericAPIView):
    # ... existing code ...

    def get(self, request):
        serializer = self.get_serializer(
            waste_collection,
            many=True
        )
        return Response(serializer.data)

    @transaction.atomic
    def post(self, request):
        data = request.data
        serializer = self.get_serializer(data=data)