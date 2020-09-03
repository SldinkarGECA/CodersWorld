from django.shortcuts import render

# Create your views here.
from .models import Homepage


def homepage(request):
    categories = Homepage.objects
    return render(request, 'homepage/homepage.html', {'categories': categories})
