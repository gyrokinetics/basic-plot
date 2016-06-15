#!/usr/bin/env python
import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "basic-plot",
    version = "0.1",
    author = "Ferdinand van Wyk, Edmund Highcock",
    description = ("A basic plotting package for GS2 output."),
    license = "MIT",
    keywords = "example pytest tutorial sphinx",
    packages=['basic_plot', 'tests', 'docs'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
    ],
)
