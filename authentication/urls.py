from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import CustomUserViewSet

# Create a router and register the viewset
router = DefaultRouter()
router.register(r'', CustomUserViewSet, basename='signup')

urlpatterns=[
    path('',include(router.urls))
]