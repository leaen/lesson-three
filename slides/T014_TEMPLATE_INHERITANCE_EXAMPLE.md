## Template Inheritance Example

* In the templates that we've created, we could optimize our template by creating title blocks and content blocks as follows: 

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

