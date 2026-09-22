from apps.accounts.models import User
from apps.accounts.api.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    print(serializer.data)
    return Response(serializer.data)

@api_view(['POST'])
def register_user(request):
    data = request.data
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        user=serializer.save()
        user.set_password(data['password'])
        user.save()
        return Response({'message': 'User registered successfully'})
    
