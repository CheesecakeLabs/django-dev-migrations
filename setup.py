from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install

from django_nomad.git.install_hook import install_checkout_hook


class LocalCheckoutHookCommand(develop):
    def run(self, *args, **kwargs):
        install_checkout_hook()
        super().run()


class InstallCheckoutHookCommand(install):
    def run(self):
        install_checkout_hook()
        super().run()


setup(
    author="Bernardo Smaniotto",
    author_email="bernardo@cheesecakelabs.com",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
    ],
    description="Easily handle migrations in dev mode",
    url="https://github.com/CheesecakeLabs/django-nomad",
    include_package_data=True,
    install_requires=["django"],
    name="django-nomad",
    packages=find_packages(),
    version="0.1.0",
    cmdclass={"local": LocalCheckoutHookCommand, "install": InstallCheckoutHookCommand},
)
