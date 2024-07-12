from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UserSerializer

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(request.data['password'])
        user.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': serializer.data
        })
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response("Invalid credentials", status=status.HTTP_401_UNAUTHORIZED)
    refresh = RefreshToken.for_user(user)
    serializer = UserSerializer(user)
    return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'user': serializer.data
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed!")


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):
    try:
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_401_UNAUTHORIZED)