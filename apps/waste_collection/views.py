from django.shortcuts import render
from django.db import transaction

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.waste_collection.api.permission import IsCustomerOrAdmin


class UserCollectionRequestView(GenericAPIView):

    def get(self, request):
        waste_collection = self.get_queryset()

        serializer = self.get_serializer(
            waste_collection,
            many=True
        )

        return Response(serializer.data)

    @transaction.atomic
    def post(self, request):
        data = request.data

        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            collection_request = serializer.save()
            create_collector_assignment(collection_request)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
