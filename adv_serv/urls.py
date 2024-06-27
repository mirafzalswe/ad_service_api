from django.urls import path
from .views import AdDetail





urlpatterns = [
    path('ads/<int:ad_id>/', AdDetail.as_view(), name='ad-detail'),
]