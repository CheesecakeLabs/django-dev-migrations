from setuptools import setup, find_packages


setup(
    author='Bernardo Smaniotto',
    author_email='bernardo@cheesecakelabs.com',
    classifiers=['Development Status :: 1 - Planning',
                 'Environment :: Web Environment',
                 'Framework :: Django',
                 'Intended Audience :: Developers',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 3',
                 'Topic :: Utilities'],
    description='Easily handle migrations in dev mode',
    include_package_data=True,
    install_requires=[],
    name='django-dev-migrations',
    packages=find_packages(),
    version='0.0.1'
)