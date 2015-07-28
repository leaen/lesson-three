## The URL Tag

* It is possible to pass a list of objects as a variable into your template.
* You could loop through that list using a `template tags`. 
    * Template tags are surrounded by `{%` and `%}`
    * Template tags have both open and close tags

For example:
```
<html>
    <head>
        <title>Albums</title>
    </head>
    <body>
        {% for album in albums %}    
        <tr>
            <td> <a href="album/{{album.id}}"> {{ album.name }} </a> </td>
        </tr>
        {% endfor %}        
    </body>
<html>

## 'album/album_list.html'    
```

