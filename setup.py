# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Tally',
    version='0.1.0',
    description='A simple web app to keep score.',
    long_description=readme,
    author='Marijn van der Zee',
    author_email='marijn@serraict.com',
    url='https://github.com/kennethreitz/samplemod',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

