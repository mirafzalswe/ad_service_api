from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Ad
from .serializers import AdSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class AdDetail(generics.RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    lookup_field = 'ad_id'




@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Both username and password are required'}, status=400)
    user = User.objects.create_user(username=username, password=password)
    token = Token.objects.create(user=user)
    return Response({'user_id': user.id, 'username': user.username, 'token': token.key}, status=201)

