twentytab-inspectmodel
======================

A django app based on django-inspect-model that implements a user interface to inspect all models in your applications.

You can find django-inspect-model documentation here: https://github.com/magopian/django-inspect-model

## Installation

Use the following command: <b><i>pip install twentytab-inspectmodel</i></b>

## Configuration

- settings.py

```py
INSTALLED_APPS = {
    ...,
    'inspectmodel',
    ...
}
```

- urls.py

```py
urlpatterns = patterns('',
    ... ,
    (r'', include('inspectmodel.urls')),
    ...
)

```

- Static files

Run collectstatic command or map static directory. If you use uWSGI you can map static files:

```ini
static-map = /static/inspectmodel/=%(path_to_site_packages)/inspectmodel/static/inspectmodel
```


To use the application you need to follow the link "http://myapplication_url/admin/inspect/browse/"