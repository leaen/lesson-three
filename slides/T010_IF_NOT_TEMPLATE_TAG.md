## The If Template Tag

* We could also use `if not` for additional control of our template

* For example:

```
<html>
    <head>
        <title>{{ album.name }}</title>
    </head>
    <body>    
        <tr>
            <td> {{ album.name }} </td>
            <td> {{ album.tracks }} </td>
            {% if not album.length %}
                <td> We don't have album length info </td>
            {% else %}
                <td> {{ album.length }} minutes </td>
            {% endif %}
        </tr>
    </body>
<html>

## 'album/album_details.html'   
```

