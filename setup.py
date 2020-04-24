#!/usr/bin/env python


import setuptools


setuptools.setup(
    name="alpha1p",
    version="0.0.1",
    author="Popescu Aura",
    author_email="popescuauraloredana@gmail.com",
    description="Class to control Ubtech Alpha1P robot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    install_requires=['pybluez'],
    python_requires='>=3.6',
)
