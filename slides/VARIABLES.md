## Variable Constructs

* A variable outputs a value from the context, which is a dict-like object mapping keys to values.
* Variables are surrounded by {{ and }}

For example:

```
from django.shortcuts import render

def hello_word(request):
    '''
    Renders your name in a template
    '''
    name = request.GET.get('name', 'party people')
    render(request, 'timetracker/hello_world.html', {'name': name})

## entries/views.py


<html>
    <head>
        <title>Timetracker</title>
    </head>        
    <body>
        <h1>Hello {{ name }}</h1>
    </body>
</html>        

## 'timetracker/hello_world.html'
```

