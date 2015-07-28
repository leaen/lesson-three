## An Object as a Context Variable

* It is also possible to pass an object as a variable into your template.

For example:

```
from django.db import models

class Album(models.Model):
    name = models.CharField(max_length=200)
    tracks = models.IntegerField(max_length=10)
    length = models.CharField(max_length=10, blank=True)

    def __unicode__(self):
        '''
        The objects title is the record's name
        '''
        return self.name


## album/models.py

from django.shortcuts import render
from .models import Album

def album_details(request, pk):
    '''
    Returns the album page
    '''
    album = Album.objects.get(pk=pk)
    return render(request, 'album/album_details.html', {'album': album}))

## album/views.py

<html>
    <head>
        <title>{{ album.name }}</title>
    </head>
    <body>    
        <tr>
            <td> {{ album.name }} </td>
            <td> {{ album.tracks }} </td>
            <td> {{ album.length }} </td>
        </tr>
    </body>
<html>

## 'album/album_details.html'    
```

