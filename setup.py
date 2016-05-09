#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# FTW
# Setup file for FTW
#

import sys
from distutils.core import setup
from pyftw import common.data.version as ftw_ver

if sys.version_info.major <= 2:
	print("ftw is not compatible (at the moment) with Python 2 :(")
	sys.exit(1)

def get_readme():
	with open("README.md") as r:
		return r.read()

setup(name="ftw", version=ftw_ver,
		description="Terminal tweeting, FTW!",
		long_description=get_readme(),
		keywords="twitter terminal ftw tweet",
		author="Federico Damián Schonborn",
		author_email="federicodamians@gmail.com",
		url="https://github.com/feskyde/ftw",
		license="GPLv2",
		py_modules=["pyftw.__main__", "pyftw.__init__",
					"pyftw.common", "pyftw.oauth", "pyftw.wrapper"],
		scripts=["ftw"],
		)
