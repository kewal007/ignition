
from rest_framework import viewsets
from .models import University,Course,Category
from .serializers import UniversitySerializer,CategorySerializer,CourseSerializer

#viewset to handle universites detail
class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

#viewset to handle courses detail
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

#viewset to handle category details
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
