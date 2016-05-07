#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# FTW
# Program data module
#

import sys

class data:
	app_name = "FTW in Shell"
	short_name = "ftw"
	version = "1.1.1"
	codename = "Albatross"
	key = "hQGQlPsTIN7iIsLVe6aHXycF0"
	key_secret = "3vZ7Q1kPf3zkIBJEKxEL9FJr9WItEzmMz8ZjiU6Ozxm3tnSjJF"

class check:
	def pyver():
		if sys.version_info.major <= 2:
			print("ftw is not compatible (at the moment) with Python 2 :(")
			sys.exit(1)
