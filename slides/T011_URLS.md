## The URL Tag

* The URL tag returns an absolute path reference (a URL without the domain name) matching a given view function and optional parameters
* With url tags you could change the path of the url and as long as you keep the url name you will access the same view
* URL tags have this format `{% url <url-name> <arguments> %}`


For example:
```
from django.conf.urls import include, url
from django.contrib import admin
from album.views import hello_world, album_list, album_details

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', hello_world, name='hello-world' ),
    url(r'^albums', album_list, name='album_list'),
    url(r'^album/(?P<pk>\d+)/$', album_details, name='album_details')
]

## music/urls.py

<html>
    <head>
        <title>Albums</title>
    </head>
    <body>
    {% if albums %}
        {% for album in albums %}  
        <tr>
            <td> <a href="{% url album-details album.id %}"> {{ album.name }} </a> 
            </td>
            <td> {{ album.tracks }} </td>
            <td> {{ album.length }} </td>
        </tr>
        {% endfor %}
    {% else %}
        <p> Add your favorite albums </p>
    {% endif %}                        
    </body>
<html>

## album/album_list.html    
```

