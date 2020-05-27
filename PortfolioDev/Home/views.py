from django.shortcuts import render

# Create your views here.

from .models import Profile

def home(request):
    profile = Profile.objects
    return render(request, 'home.html', {'profile': profile})

