from core.views import ProductViewSet, ServiceViewSet, ProjectListAPIView
from django.urls import path
from rest_framework.routers import DefaultRouter

from rest_framework import routers

router = DefaultRouter()
urlpatterns = [
    path('products/', ProjectListAPIView.as_view())
] + router.urls

router = routers.DefaultRouter()
router.register('products/', ProductViewSet, base_name='core')
router.register('services/', ServiceViewSet, base_name='core')



