import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__)), 'README.rst') as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
