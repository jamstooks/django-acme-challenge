#!/usr/bin/env python
from setuptools import setup, find_packages
import os


# Utility function to read README file
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-acme-challenge',
    version='1.2',
    description="A quick tool to serve the acme-challenge verification page.",
    author='Benjamin W Stookey',
    author_email='ben.stookey@gmail.com',
    url='https://github.com/jamstooks/django-acme-challenge',
    long_description=read("README.md"),
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
    ],
    test_suite='tests.main',
    install_requires=['Django',],
)
