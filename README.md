# Django Nomad

A Django extension to make your life easier when dealing with migrations in multiple branches.

## Installing

Install via pip:
```
pip install django-nomad
```

Add django nomad to the INSTALLED_APPS on settings.py:
```
INSTALLED_APPS = (
  ... other django apps ...,
  'django_nomad',
)
```

Add the git-hook to your project:
```
python manage.py install_nomad_git_hook
```

## Contributing

Before getting started, please install the project dependencies and after that enbale Flake8's git
commit hook:

```
python -m flake8 --install-hook git
```
