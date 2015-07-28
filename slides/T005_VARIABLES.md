## Variable Constructs

* We could also add variable(s) to our template by passing a dict into the render method 
* A variable outputs a value from the context, which is a dict-like object mapping keys to values.
* Variables are surrounded by `{{` and `}}`

For example:

```
from django.shortcuts import render

def hello_world(request):
    '''
    Renders your name in a template
    '''
    name = request.GET.get('name', 'party people')
    return render(request, 'album/hello_world.html', {'name': name})

## album/views.py


<html>
    <head>
        <title>Hello World</title>
    </head>        
    <body>
        <h1>Hello {{ name }}</h1>
    </body>
</html>        

## 'album/hello_world.html'
```

