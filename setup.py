#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
REQUIREMENTS = open(os.path.join(os.path.dirname(__file__), 'requirements.txt')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-spirit-air',
    version='0.1',
    description='A Spirit forum theme inspired by fluxbb\'s Air',
    author='MGXRace',
    author_email='kalhartt@gmail.com',
    long_description=README,
    url='http://github.com/MGXRace/Spirit-Air/',
    packages=find_packages(exclude=['example', ]),
    entry_points='''
    [spirit.themes]
    Air=air:Air''',
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    license='MIT License',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
