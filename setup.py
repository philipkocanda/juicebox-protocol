# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='juicebox',
    packages=find_packages(exclude=('tests', 'tests.*')),
    version='0.0.1',
    license='MIT',
    description='Juicebox is a library to communicate with Enel X Juicebox devices over the local network',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Philip Kocanda',
    author_email='philip@kocanda.nl',
    url='https://github.com/philipkocanda/juicebox',
    download_url='https://github.com/philipkocanda/juicebox/archive/refs/tags/v0.1.1.zip',
    keywords=['juicebox', 'iot'],
    install_requires=[],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.11',
    ],
)
