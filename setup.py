from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install

from django_nomad.git.install_hook import install_checkout_hook


class LocalCheckoutHookCommand(develop):
    def run(self, *args, **kwargs):
        install_checkout_hook()
        develop.run(self)


class InstallCheckoutHookCommand(install):
    def run(self):
        install_checkout_hook()
        install.run(self)


setup(
    author="Bernardo Smaniotto",
    author_email="bernardo@cheesecakelabs.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Utilities",
    ],
    description="Easily handle migrations in dev mode",
    url="https://github.com/smaniotto/django-nomad",
    include_package_data=True,
    install_requires=["django"],
    name="django-nomad",
    packages=find_packages(),
    version="0.1.2",
    cmdclass={"local": LocalCheckoutHookCommand, "install": InstallCheckoutHookCommand},
)
