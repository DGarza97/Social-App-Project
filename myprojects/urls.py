from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed_page, name='feed'),
    path('myprojects/', views.myprojects, name='myprojects')
]