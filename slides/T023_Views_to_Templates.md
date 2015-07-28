# Views to Templates
Examples:
```
def album(request, album_id=1):
    return render_to_response('albums.html',
                            {'album': Album.Objects.get(id=album_id)})
```
```
def songs(request):
    return render_to_response('songs.html',
                            {'songs': Songs.objects.all()})
```



