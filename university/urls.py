from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import UniversityViewSet,CourseViewSet,CategoryViewSet

# Create a router and register the viewset
router = DefaultRouter()
router.register(r'',UniversityViewSet ,basename='university')
router.register(r'courses',CourseViewSet ,basename='course')
router.register(r'categories',CategoryViewSet ,basename='category')

urlpatterns=[
    path('',include(router.urls))
]