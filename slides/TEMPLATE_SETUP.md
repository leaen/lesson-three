## Configuring your Templates

* Django Settings contains a Templates variable that allows you to configure you settings.

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'timetracker/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

* The `DIRS` key has a list of path values that Django will search to find your templates

* In this case we told Django to search in the timetracker/timetracker/templates directory.
