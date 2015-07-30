### MelbDjango School - Lesson Three

Django Views, URLs & Templates

---

### WIFI

Common Code / cc&20!4@

---

### Django Views

- Django views are where our application logic lives
- They process a HTTP Request and return a HTTP Response
- By convention we place our views in `views.py`
- Django provides two core types of views:
  - Function based views
  - Class based views

---

### Function Based Views

- Today we're focused on function based views (FBVs)
- FBVs are the simpler of the two types of views
- All FBVs accept a `HttpRequest` object as the first argument

---

### A Simple Django View

- Here's an example from our Lesson One homework:

```
from django.http import HttpResponse

def hello_world(request):
    name = request.GET.get('name')
    if name:
        return HttpResponse('Hello %s' % name)
    else:
        return HttpResponse('<form><input name="name"></form>')
```

---

### The Django logic layer

- We use views to control the logic of our application
  - Deciding what to return to the user
  - Validating input
  - Getting and updating models from our database
  - Anything else you can think of...

---

### Django URLs

- Django projects include a `URLconf` that define a list of URLs it knows about
- Django searches through this list and returns the first one that matches the request's URI
- By default, our URLs live in `<project-name>/urls.py`
- We can include other URLs files for our Django applications

---

### Django's default URLs

- Simplified in Django 1.8
- Django enables /admin/ by default by including its URLConf

```
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]
```

Check out the top of your `urls.py` - it's a cheat sheet to using URLs

---

### Adding a new URL

- We can add a URL that points to a view

- URLs that point to a view include three parts:
  - the URL pattern
  - the view
  - the URL's name

- URL patterns are regular expressions
  - Check out the resources if you're not familiar

```
from django.conf.urls import include, url
from django.contrib import admin

import albums.views

urlpatterns = [
    url(r'^albums/$', albums.views.albums, name="albums"),
    url(r'^admin/', include(admin.site.urls)),
]
```

---

### Capturing dynamic parts of the URL

- Django lets you capture parts of the URL to be passed to your views
  - Simply put parenthesis around the part you want

```
urlpatterns = [
    url(r'^albums/$', albums.views.album_list, name="album_list"),
    url(r'^albums/([0-9]+)/$', albums.views.album_detail, name="album_detail"),
    url(r'^admin/', include(admin.site.urls)),
]
```

---

### Capturing dynamic parts of the URL

- You can optionally _name_ the captured parts
  - Use the `(?P<name>pattern)` syntax

- The captured parts will be passed to your view as keyword arguments

```
urlpatterns = [
    url(r'^albums/$', albums.views.album_list, name="album_list"),
    url(r'^albums/(?P<album_id>[0-9]+)/$', albums.views.album_detail, name="album_detail"),
    url(r'^admin/', include(admin.site.urls)),
]
```

---

### Including other urls.py files

- It's best practice to create `urls.py` files for each of your applciations
- You need to include those in the root URLconf of your project
- Make sure you remove the `$` from the pattern when using include

```
from albums import urls as album_urls

urlpatterns = [
    url(r'^albums/', include(album_urls)),
    url(r'^admin/', include(admin.site.urls)),
]
```

---

### What is a Django template?

- A convenient way to generate dynamic HTML (and XML, CSV, JSON, etc.)
- Allows special syntax to let you insert non-static content
  - Variables
  - Tags
  - Filters
  - Comments
- Supports template inheritance and includes
- Django includes backends for the Django Template Language (DTL) and Jinja2

---

### Configuring Template Settings

- **New in Django 1.8** we have a `TEMPLATES` setting dictionary in our `settings.py` file
- The template settings allow developers to plug-in different template backends (DTL, Jinja2, ...)
- `DIRS` allows us to search specific directories for template files
- `APP_DIRS` tells Django whether or not to look in our apps for templates

---

### Configuring Template Settings

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            # ... some options here ...
        },
    },
]
```

---

We noticed a few people did something like this in their Lesson One homework:

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
          os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {},
    },
]
```

Nice one!

---

### Template Hierarchy

- Assuming a project named `music` and an app named `albums`
- The Django convention is to add a templates directory:  

```
├── manage.py
├── albums
│   ├── admin.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── templates
│   │   └── template.html
│   ├── tests.py
│   └── views.py
└── music
    ├── __init__.py
    ├── settings.py
    ├── tests.py
    ├── urls.py
    └── wsgi.py
```

---

### Django Template Language

- DTL was the only template language supported by Django until Django 1.8
- Opinionated and forces you to focus on presentation only
- Designed to feel comfortable to those used to working with HTML
- Introduces special syntax to allow dynamic content from our views
- What we'll be using throughout this course

---

### Rendering Templates

- There are a few ways to render templates in Django
- Since 1.8 these two are what you'll normally use:
  - `django.shortcuts.render`
  - `django.template.loader.get_template`

---

### django.shortcuts.render

```
from django.shortcuts import render

def hello_world(request):
  return render(request, 'hello.html', {'name': 'world'})
```

- `render` returns a HttpResponse object
- Optionally accepts `status` and `content_type` (and a bunch of other options)

---

### django.template.loader.get_template

```
from django.template.loader import get_template

def hello_world(request):
  template = get_template('hello.html')
  html = template.render({'name': 'world'}, request)
  return HttpResponse(html)
```

- `get_template` returns a Template object
- `request` is optional using this method
- `.render()` returns a string representation of the rendered template


---

### A Quick Example

- An example of a template that we could have used in our Hello World homework from Lesson One

```
<html>
  <head>
    <title>Hello World</title>
  </head>
  <body>
    {% if name %}
      <h1>Hello {{ name }}!</h1>
    {% else %}
      <h1>Say Hello</h1>
      <form>
        <input name="name" />
        <input type="submit" />
      </form>
    {% endif %}
  </body>
</html>
```

---

### Template Variables

- The easiest way to get content into your template
- Variables are surrounded by `{{` and `}}`
- The come from the **template context**

- Let's use the view from before:

```
from django.shortcuts import render

def hello_world(request):
  return render(request, 'hello.html', {'name': 'world'})
```

---

### Template Variables

- And (a slightly simpler) HTML template:


```
<html>
  <head>
    <title>Hello World</title>
  </head>
  <body>
      <h1>Hello {{ name }}!</h1>
  </body>
</html>
```

---

### Template Variables

- Which will result in this HTML:

```
<html>
  <head>
    <title>Hello World</title>
  </head>
  <body>
      <h1>Hello world!</h1>
  </body>
</html>
```

- Simple, right?

---

### Template Variables

- You can use the "dot syntax" (`object.attribute`) to access attributes and functions on objects

```
<html>
  <head>
    <title>{{ album.name }}</title>
  </head>
  <body>
    <table>
      <tr>
        <td>{{ album.artist }}</td>
        <td>{{ album.name }}</td>
        <td>{{ album.tracks }}</td>
        <td>{{ album.length }}</td>
      </tr>
    </table>
  </body>
<html>
```

---

### Template Variables

- Which could result in something like:

```
<html>
  <head>
    <title>Homework</title>
  </head>
  <body>
    <table>
      <tr>
        <td>Daft Punk</td>
        <td>Homework</td>
        <td>16</td>
        <td>73:53</td>
      </tr>
    </table>
  </body>
<html>
```

---

### Template Tags

- What if we want to check if something exists before we use it?
- Or iterate over a collection of things?
- Or extend another template instead of including everything every time?

---

### Template Tags

- That's where Django's template tags come in!
- Tags allow us to add logic to our templates
- Tags are surrounded by `{%` and `%}`

---

### Checking for true/false values

- The `{% if %}` tag lets us check if a variable is "true"
- "true" in this sense means anything that is:
  - not None
  - not false
  - exists

```
{% if name %}
  <h1>Hello {{ name }}</h1>
{% endif %}
```

---

### Checking for true/false values

- You can extend this easily with `{% else %}`

```
<html>
  <head>
    <title>Hello World</title>
  </head>
  <body>
    {% if name %}
      <h1>Hello {{ name }}!</h1>
    {% else %}
      <h1>Say Hello</h1>
      <form>
        <input name="name" />
        <input type="submit" />
      </form>
    {% endif %}
  </body>
</html>
```

---

### Looping through objects

- We can loop through arrays and other iterables by using:

```
{% for object in iterable %}
  {{ object.name }}
{% endfor %}
```

- (you'll normally want to name things a little better that I have)
- And don't forget the `{% endfor %}`

---

### Looping through objects

- So, if we create a view that returns a QuerySet:

```
from django.shortcuts import render
from .models import Album

def albums(request):
  album_list = Album.objects.all()
  return render(request, 'albums.html', {'album_list': album_list})
```

---

### Looping through objects

- We can create a template with a `{% for %}` tag in it:

```
<!doctype>
<html>
  <head>
    <title>Albums</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
  </head>
  <body>
    <table class="table">
      <tr>
        <th>Artist</th><th>Name</th><th>Tracks</th><th>Length</th>
      </tr>

      {% for album in album_list %}
        <tr>
          <td>{{ album.artist }}</td>
          <td>{{ album.name }}</td>
          <td>{{ album.tracks }}</td>
          <td>{{ album.length }}</td>
        </tr>
      {% endfor %}
    </table>
  </body>
<html>
```

---

![](http://i.imgur.com/R3GyG5m.png)

---

### Inheriting from other templates

- By using a combination of `{% extends %}` and `{% block %}` we can enable template inheritance
- This allows us to create base templates to use as a skeleton
- You can (optionally) override **blocks** in your child template

---

### Inheriting from other templates

- Imagine that our `base.html` template looks like this:

```
<!doctype>
<html>
  <head>
    <title>{% block title %}{% endblock %}</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
  </head>
  <body>
    {% block content %}
    {% endblock %}
  </body>
<html>
```

---

### Inheriting from other templates

- Then we could have an `albums.html` template like this:

```
{% extends 'base.html' %}
{% block title %}Albums{% endblock %}

{% block content %}
<table class="table">
  <tr>
    <th>Artist</th><th>Name</th><th>Tracks</th><th>Length</th>
  </tr>

  {% for album in album_list %}
    <tr>
      <td>{{ album.artist }}</td>
      <td>{{ album.name }}</td>
      <td>{{ album.tracks }}</td>
      <td>{{ album.length }}</td>
    </tr>
  {% endfor %}
</table>
{% endblock %}
```

---

### Using URLs in templates

- The `{% url %}` tag lets us reverse URLs based on the `name` in our `urls.py`
- You can pass parameters to fill in values in the URL

---

### Using URLs in templates

- In urls.py:

```
url(r'^albums', album_list, name='album_list'),
url(r'^album/(?P<pk>\d+)/$', album_details, name='album_details')
```

- In your template:

```
<a href="{% url 'album_list' %}">Albums</a>
<a href="{% url 'album_details' album.id %}">{{ album.name }}</a>
```
