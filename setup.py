#!/usr/bin/env python

from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages
setup(
    name = "halng",
    version = "0.5",
    author = "Peter Teichman",
    license = "MIT",
    packages = find_packages(exclude=["tests"]),
    test_suite = "tests.halng_suite",
)