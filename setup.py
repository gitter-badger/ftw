#!/usr/bin/env python3
#
# setup.py for Fast Tweet
#

from distutils.core import setup

setup(name="ftw",
      version="1.0",
      description="Terminal tweeting, FTW!",
      author="Federico Damián Schonborn",
      author_email="federicodamians@gmail.com",
      url="https://github.com/feskyde/ftw",
      py_modules=["ftw", "fastw.twitter", "fastw.echo"],
      install_requires=["twitter"],
      )
