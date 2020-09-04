from django.shortcuts import render

from .models import Homepage


def homepage(request):

    categories = Homepage.objects
    return render(request, 'homepage/homepage.html', {'categories': categories})
