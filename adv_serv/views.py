from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Ad
from .serializers import AdSerializer

class AdDetail(generics.RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    lookup_field = 'ad_id'