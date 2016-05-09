#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# FTW
# Main module
#

import os
import argparse
from pyftw import common, oauth, wrapper

common.checks.py_ver()

parser = argparse.ArgumentParser(prog="ftw", description="terminal tweeting, ftw!")
parser.add_argument("text", type=str, nargs="?", help="tweet text")
parser.add_argument("-i", "--image", metavar="file", nargs="+", help="add one or more images")
parser.add_argument("-u", "--url", metavar="url", help="add a shortened url")
parser.add_argument("-s", "--shortener", metavar="shortener", default="tinyurl", help="change the shortener (defaults to tinyurl)")
parser.add_argument("-v", "--version", action="store_true", help="show version")

args = parser.parse_args()

def ftw_main():
	if args.version:
		common.printer.ver(data.app_name, data.short_name, data.version, data.codename)
	elif args.text:
		encoded = args.text.encode("utf-8")
		if args.image:
			length = len(args.image)
			if length == 1:
				wrapper.post.one_image(encoded, args.image)
			elif length >= 2 and length < 5:
				wrapper.post.multi_images(encoded, args.image)
			elif length >= 5:
				common.printer.die("the maximium supported images are 4")
		elif args.url:
			if args.shortener:
				shortened_url = wrapper.shortener.make_short(args.url, args.shortener)
			else:
				shortened_url = wrapper.shortener.make_short(args.url, "tinyurl")
				wrapper.post.text_only(encoded + "" + sortened_url)
		else:
			wrapper.post.text_only(encoded)
	else:
		common.printer.die("please insert any argument (use -h if you need help)")

ftw_main()
