from django.urls import path
from .views import AdDetail
from .views import create_user




urlpatterns = [
    path('ads/<int:ad_id>/', AdDetail.as_view(), name='ad-detail'),
    path('create_user/', create_user, name='create_user'),

]