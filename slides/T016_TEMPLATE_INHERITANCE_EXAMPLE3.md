## Template Inheritance Example Part 3

* We could then do the same thing to our album_details.html template but in this case we will overwrite the original content in our `{% block title %}` tag  

```
{% extends "base.html" %}

{% block title %} {{ album.name }} {% block title %}

{% block content %}
    <tr>
        <td> {{ album.name }} </td>
        <td> {{ album.tracks }} </td>
        {% if not album.length %}
            <td> We don't have album length info </td>
        {% else %}
            <td> {{ album.length }} minutes </td>
        {% endif %}
    </tr>
{% endblock content %}

## album/album_list.html   
```

