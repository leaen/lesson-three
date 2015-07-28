## Template Inheritance Example

* We could optimize our templates by creating a base template from which the other template could inherit
* The base template will have a title and content block 

```
<html>
    <head>
        <title>
            {% block title %} Albums {% endblock title %}
        </title>
    </head>
    <body>
    {% block content %}
    {% endblock content %}                        
    </body>
<html>

## template/base.html    
```

