from django.urls import path, include
import authentication,university

#url patterns for all the api's of the project
urlpatterns = [
    path('api/users/', include('authentication.urls')), 
    path('api/universities/', include('university.urls')), 
]