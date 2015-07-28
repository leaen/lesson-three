Django uses a Python module called a URLconf (URL configuration) to map between URL patterns (simple regular expressions) to Python functions (i.e. your views).

When writing regular expressions in Python it is always done with r in front of the string - this is to indicate Python that the string may contain special characters that are not meant for Python itself but are instead part of the regular expression.

Examples:
```
from django.conf.urls import url
from music.views import list_of_views

urlpatterns = [
    url(r'^$', my_homepage_view),
    # ...
]
```

