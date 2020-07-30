from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def home(request):
    return render(request, 'usa/home.html')

def affordable_housing(request):
    return render(request, 'usa/affordable-housing.html')

def printing(request):
    return render(request, 'usa/3d-printing.html')

def about_hupi(request):
    return render(request, 'usa/about-hupi.html')

def about_winsun(request):
    return render(request, 'usa/about-winsun.html')