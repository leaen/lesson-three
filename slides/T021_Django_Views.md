# What are Views in Django?

- Django View is a python function that takes a web request and returns a web response[Can be a Web page, a redirect, Status, image etc].
- A View contains logic to return a response. 
- The convention is to put views in views.py file. Its not compulsory though.

Example:
```
def call_this_code_1(request):
    # Find particular album or Song etc ...
    # Get all Titles of the ablums
    return HTTPResponse('Return Something meaningful')
```

