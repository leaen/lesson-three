## Template Inheritance Example Continued

* We could then extend our base.html template into our album_list.html using the `{% extends %}` tag and customise the content using the `{% block content %}` tag  

```
{% extends "base.html" %}

{% block content %}
    {% if albums %}
        {% for album in albums %}
        <tr>
            <td> <a href="{% url 'album_details' album.id %}"> {{ album.name }} </a>
            </td>
            {% comment "No need for this info since we have a details page" %}
            <td> {{ album.tracks }} </td>
            <td> {{ album.length }} </td>
            {% endcomment %}
        </tr>
        {% endfor %}
    {% else %}
        <p> Add your favorite albums </p>
    {% endif %}
{% endblock content %}

## album/album_list.html   
```

