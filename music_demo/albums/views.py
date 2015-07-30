from django.shortcuts import render
from .models import Album


def albums(request):
  album_list = Album.objects.all()
  return render(request, 'albums.html', {'album_list': album_list})
