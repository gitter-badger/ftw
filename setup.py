#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# FTW
# Setup file for FTW
#

import sys
from distutils.core import setup

if sys.version <= (2, 7):
	print("ftw is not compatible (at the moment) with Python 2 :(")
	sys.exit(1)

def get_readme(readme):
	with open(readme) as r:
		return r.read()

setup(name="ftw", version="1.2",
		description="Terminal tweeting, FTW!",
		long_description=get_readme("README.md"),
		keywords="twitter terminal ftw tweet",
		author="Federico Damián Schonborn",
		author_email="federicodamians@gmail.com",
		url="https://github.com/feskyde/ftw",
		license="GPLv2",
		py_modules=["pyftw.__main__", "pyftw.__init__",
					"pyftw.oauth", "pyftw.printer", "pyftw.program",
					"pyftw.twitter", "pyftw.shortener"],
		install_requires=["twitter", "pyshorteners"],
		scripts=["ftw"],
		)
