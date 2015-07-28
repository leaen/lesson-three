## Variables and Template Tags

* It is possible to pass a list of objects as a variable into your template.
* You could loop through that list using a `template tags`. 
    * Template tags are surrounded by `{%` and `%}`
    * Template tags have both open and close tags

For example:
```
from django.shortcuts import render

def album_list(request):
    '''
    Returns the album page
    '''
    albums = Album.objects.all()
    return render(request, 'album/album_list.html', {'albums': albums})

## album/views.py

<html>
    <head>
        <title>Albums</title>
    </head>
    <body>
        {% for album in albums %}    
        <tr>
            <td> <a href="album/{{album.id}}"> {{ album.name }} </a> </td>
            td> {{ album.tracks }} </td>
            <td> {{ album.length }} </td>
        </tr>
        {% endfor %}        
    </body>
<html>

## 'album/album_list.html'    
```

