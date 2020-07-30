from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('affordable-housing/', views.affordable_housing),
    path('3d-printing/', views.printing),
    path('about-hupi/', views.about_hupi),
    path('about-winsun/', views.about_winsun),
]