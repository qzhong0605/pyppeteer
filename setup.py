#!/usr/bin/env python

from distutils.core import setup
from pyppeteer import version

setup(
    name = "pyppeteer",
    version = version,
    packages = ["pyppeteer"]
)
