#!/usr/bin/env python

from os import path

from setuptools import setup


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="gallery657",
    version='2021.10.18a0',
    description='A small image gallery app, with Vue frontend and Django backend.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Oscar F',
    url='https://github.com/oscfr657/Gallery657',
    packages=['gallery657'],
    package_dir={'gallery657':'.'},
    package_data={'gallery657': [
        './migrations/*',
        './static/*/*/*',
        './static/*/*/*/*',
        './templates/*',
        ]
    },
    include_package_data=True,
    install_requires=[
        'Django>=1.11.3',
        'pytz>=2017.2',
        'djangorestframework>=3.6.3',
        'Pillow>=4.2.0',
        'python-magic>=0.4.13',
    ],
    license='Hippocratic License Version Number: 2.1 with Commons Clause License Condition v1.0',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Framework :: Django',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)