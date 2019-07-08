# Django Nomad

A Django extension to make your life easier when dealing with migrations in multiple
branches.

## Definition

A Nomad database migration happens when schema changes are applied to the database, but
are not reflected on migration nor models files.

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

A post-checkout git-hook will be added to your project.

NOTE: to completely uninstalling the package, you have to delete
`.git/hooks/post-checkout`

## Contributing

Before getting started, please install the project dependencies and enable black auto-
formatter on your editor of choice.

### Running tests

Simply run:

```
pytest
```

For running tests on multiple python and django versions, use:

```
tox
```

Note: you need to have python3.4, python3.5, python3.6 and python3.7 installed in your
PATH. If you use pyenv, simply run `pyenv global <3.4.x> <3.5.x> <3.6.x> <3.7.x>` and
install tox on your python system version.

There's a full Django project under `tests/tests_project`, including git versioning and
a SQLite database file. It is intended to make it easier to emulate a real-world
scenario of checking out from a branch with Nomad migrations. The `dot.git` folder is
actually the `.git` folder used by git to control refs, it is renamed to `.git` during
tests. There are two branched in this project: `master` and `newbranch`. In the code
referenced by `newbranch`, there's a Nomad migration and the pre-checkout hook should
print a error message when checking out to `master`.
