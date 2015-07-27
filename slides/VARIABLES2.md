## Context as a Model Instance

* It is also possible to pass model instances into your template.

For example:

```
from django.shortcuts import render

def entries(request):
    '''
    Renders your name in a template
    '''
    entry = Entry.objects.get(pk=1) 
    render(request, 'timetracker/entry.html', {'entry': entry})

## entries/views.py


<html>
    <head>
        <title>Entry</title>
    </head>
    <body>    
        <tr>
            <td> {{ entry.start }} </td>
            <td> {{ entry.end }} </td>
            <td> {{ entry.user }} </td>
            <td> {{ entry.description }} </td>
            <td> {{ entry.project }} </td>
            <td>
        </tr>
    </body>
<html>

## 'timetracker/hello_world.html    
```

