## Configuring your Templates

Django is able to find your templates if one the following is implemented:

* Add a template directory inside your installed apps (only if APP_DIRS is set to True)
* Add a specific path to your template settings

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'albums/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
                #    ... some options here ...
            ],
        },
    },
]
```

* The `DIRS` key allows you to add a list of path values that Django will search to find your templates

* If our project is called music then we told Django to search in the music/albums/templates directory.
