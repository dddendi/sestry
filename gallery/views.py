from django.shortcuts import render
from .models import Photo

# Create your views here.


def index(request):
    photos = Photo.objects.order_by('-date')
    return render(request, 'gallery/gallery_home.html', {'photos': photos})
