#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

setup(
    name='django-tables2-simplefilter',
    version='0.1',
    description='Simple filters for django-tables2',
    author='Benjie Chen',
    author_email='benjie@alum.mit.edu',
    long_description=open('README.md', 'r').read(),

    install_requires=['Django >= 1.2', 'django-tables2'],
    packages=['django_tables2_simplefilter'],
    zip_safe=False,
    requires=[],
    classifiers=[
      'Environment :: Web Environment',
      'Framework :: Django',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: BSD License',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
      'Topic :: Internet :: WWW/HTTP',
      'Topic :: Software Development :: Libraries',
    ],
)

