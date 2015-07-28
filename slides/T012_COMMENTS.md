## The Comment Tag

* The comment tag allows you to comment out sections of your template
* The comment tag has an opening and closing tag:
    * `{% comment %}` 
    * `{% endcomment %}`
* An optional note may be inserted in the opening tag


For example:
```

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
            {% comment "Don't need for this info since we have a details page" %}
            <td> {{ album.tracks }} </td>
            <td> {{ album.length }} </td>
            {% endcomment %}
        </tr>
        {% endfor %}
    {% else %}
        <p> Add your favorite albums </p>
    {% endif %}                        
    </body>
<html>

## album/album_list.html    
```

