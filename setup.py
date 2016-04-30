#!/usr/bin/env python3
#
# setup.py for Fast Tweet
#

from distutils.core import setup

def get_readme(readme):
    with open(readme) as r:
        return r.read()

setup(name="ftw",
      version="1.2",
      description="Terminal tweeting, FTW!",
      long_description=get_readme("README.md"),
      keywords="twitter terminal ftw tweet",
      author="Federico Damián Schonborn",
      author_email="federicodamians@gmail.com",
      url="https://github.com/feskyde/ftw",
      license="GPLv2",
      py_modules=["ftw", "pyftw.twitter", "pyftw.shortener", "pyftw.printer"],
      install_requires=["twitter", "pyshorteners"]
      )
