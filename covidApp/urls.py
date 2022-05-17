from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('data/<str:fileCSV>/',views.datatable,name='datatable'),
    path('displayGraph/<str:g>/',views.displayGraph,name='displayGraph'),
]
