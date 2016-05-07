#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# FTW 1.3
# print() modifications
#

import sys

class color:
	none = "\033[0m"
	bold = "\033[1m"
	red = "\033[91m"
	green = "\033[92m"
	yellow = "\033[93m"

def info(msg):
	print(color.green + "[info] {}".format(msg) + color.none)

def error(msg):
	print(color.red + "[error] {}".format(msg) + color.none)
	print(color.red + "[error] exiting with code 1" + color.none)
	sys.exit(1)

def warning(msg):
	print(color.yellow + "[warning] {}".format(msg) + color.none)

def version(app, short, ver, name):
	print("{} ({}) version: {} \"{}\"".format(app, short, ver, name))
