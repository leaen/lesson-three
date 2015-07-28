## Template Settings

* New in Django 1.8 we have template settings in the projects `settings.py` file 
* The template settings allow developers to plug-in different template backend (Django Templates, Jinja2, ...)
* We could also list where our engine should search for our templates
* And other options such as `context_processors`

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

