from django.shortcuts import render

# Create your views here.
from .models import Blog

def blogs(request):
    blog=Blog.objects
    return render(request, 'blog.html', {'blog': blog})
