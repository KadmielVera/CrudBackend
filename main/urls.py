from django.urls import path
from .views import *

urlpatterns = [
    path("Crud/", CrudAPIView.as_view(), name='Crud'),
    path('Crud/<int:pk>/', CrudAPIView.as_view(), name='CrudParameters'),
]

