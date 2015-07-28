## Template Inheritance Example

* In the templates that we've created, we could optimize our templates by creating a base template with a title blocks and content blocks: 

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

