from django.urls import path
from .views import my_projects

urlpatterns = [
    path('', my_projects, name='my_projects'),
]