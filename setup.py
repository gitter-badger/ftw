#!/usr/bin/env python3
#
# setup.py for Fast Tweet
#

from distutils.core import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name="ftw",
      version="1.0.1",
      description="Terminal tweeting, FTW!",
      long_description=readme(),
      keywords="twitter terminal ftw tweet",
      author="Federico Damián Schonborn",
      author_email="federicodamians@gmail.com",
      url="https://github.com/feskyde/ftw",
      license="GPLv2",
      py_modules=["ftw", "fastw.twitter", "fastw.echo"],
      scripts=['bin/ftw'],
      install_requires=["twitter"],
      )
