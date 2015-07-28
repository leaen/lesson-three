## Render a Template

<!-- * You could render a template by using the get_template function
    * get_template takes a string path/to/template argument
    * It then creates Template object
    * You could then render that template using the Template object's render method -->

* You could render a template by using the `render` function
    * Passing in the request object
    * Passing in the template as a second argument

For example:

```
## We made a project called music and an app called album
## Inside our app directory we have a sub-directory called template

from django.shortcuts import render

def hello_word(request):
    '''
    Renders your name in a template
    '''
    return render(request, 'album/hello_world.html')

## album/views.py


<html>
    <head>
        <title>Albums</title>
    </head>        
    <body>
        <h1>Hello World</h1>
    </body>
</html>        

## 'album/hello_world.html'
```
