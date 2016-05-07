#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# FTW
# Setup file for FTW
#

import sys
from distutils.core import setup
from pyftw import program

if sys.version_info.major <= 2:
	print("ftw is not compatible (at the moment) with Python 2 :(")
	sys.exit(1)

def get_readme():
	with open("README.md") as r:
		return r.read()

setup(name="ftw", version=program.data.version,
		description="Terminal tweeting, FTW!",
		long_description=get_readme(),
		keywords="twitter terminal ftw tweet",
		author="Federico Damián Schonborn",
		author_email="federicodamians@gmail.com",
		url="https://github.com/feskyde/ftw",
		license="GPLv2",
		py_modules=["pyftw.__main__", "pyftw.__init__",
					"pyftw.oauth", "pyftw.printer", "pyftw.program",
					"pyftw.twitter", "pyftw.shortener"],
		scripts=["ftw"],
		)
