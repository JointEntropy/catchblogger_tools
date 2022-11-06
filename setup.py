"""
Установщик пакета
"""

import setuptools
from setuptools import find_packages


with open("README.md") as fh:
    long_description = fh.read()

requires = open('requirements.txt').read().split('\n')


setuptools.setup(
    name="catchblogger_tools",
    version="0.1.3",  # engine version . number of api methods . number of fixes in version
    author="Grigory Ovchinnikov",
    author_email="ogowm@hotmail.com",
    description="Catchblogger utils",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JointEntropy/catchblogger_tools",
    packages=find_packages(),
    install_requires=requires,
    setup_requires=[
        'pytest-runner',
    ]
)