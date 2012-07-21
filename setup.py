#!/usr/bin/env python
#from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name="tomthumb",
    version="0.0.1",
    description="A handy document thumbnailing tool.",
    author="Benjamin Coe",
    author_email="bencoe@gmail.com",
    url="https://github.com/bcoe/Adventures-in-Document-Thumbnailing",
    packages = find_packages(),
    install_requires = [
        'PIL'
    ],
    entry_points = {
        'console_scripts': [
            'tomthumb = tomthumb.__main__:main'
        ]
    }
)