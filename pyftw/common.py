#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# FTW
# Common module
#

import sys

class data:
	app_name = "FTW in Shell"
	short_name = "ftw"
	version = "1.1.1"
	codename = "Albatross"
	key = "hQGQlPsTIN7iIsLVe6aHXycF0"
	key_secret = "3vZ7Q1kPf3zkIBJEKxEL9FJr9WItEzmMz8ZjiU6Ozxm3tnSjJF"

class colors:
	none = "\033[0m"
	bold = "\033[1m"
	red = "\033[91m"
	green = "\033[92m"
	yellow = "\033[93m"

class printer:
	def info(msg):
		print(colors.green + "[info] {}".format(msg) + colors.none)

	def die(msg):
		print(colors.red + "[error] {}".format(msg) + colors.none)
		print(colors.red + "[error] exiting with code 1" + colors.none)
		sys.exit(1)

	def warn(msg):
		print(colors.yellow + "[warning] {}".format(msg) + colors.none)

	def ver(app, short, ver, name):
		python_major = sys.version_info.major
		python_minor = sys.version_info.minor
		print("{} ({}) version: {} \"{}\", running on Python {}.{}".format(app, short, ver, name, python_major, python_minor))

class check:
	def py_ver():
		if sys.version_info.major <= 2:
			die("ftw is not compatible (at the moment) with Python 2 :(")
			sys.exit(1)

	def if_chars(text, lenght):
	if len(text) > lenght:
		printer.die("your tweet needs to be {} characters maximium!".format(lenght), 1)
