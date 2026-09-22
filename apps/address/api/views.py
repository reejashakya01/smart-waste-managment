
from apps.address.api.serializers import AddressSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from apps.address.models import UserAddress
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def address_list(request):
    user_address = UserAddress.objects.filter(
        user = request.user
    )
    serializer = AddressSerializer(user_address, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_address(request):
    data = request.data
    serializer = AddressSerializer(data=data,context=request)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response({'message': 'Address added successfully'})
    else:
        return Response(serializer.errors, status=400)
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def address_update(request,id):
    address = UserAddress.objects.get(id=id)
    data = request.data
    serializer = AddressSerializer(address,data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message":"Address updated successfully"
        })
    else:
        return Response(serializer.errors,400)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def address_delete(request,id):
    address = UserAddress.objects.get(id=id)
    address.delete()
    return Response({"message":"Address deleted successfully"})