#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# FTW
# Main script
#

import os
import argparse
from pyftw import twitter, oauth, shortener, printer
from pyftw.program import data, check

check.pyver()

parser = argparse.ArgumentParser(prog="ftw", description="terminal tweeting, ftw!")
parser.add_argument("text", type=str, nargs="?", help="tweet text")
parser.add_argument("-i", "--image", metavar="file", nargs="+", help="add one or more images")
parser.add_argument("-u", "--url", metavar="url", help="add a shortened url")
parser.add_argument("-s", "--shortener", metavar="shortener", default="tinyurl", help="change the shortener (defaults to tinyurl)")
parser.add_argument("-v", "--version", action="store_true", help="show version")

args = parser.parse_args()

def doallthings():
	if args.version:
		printer.version(data.app_name, data.short_name, data.version, data.codename)
	elif args.text:
		encoded = args.text.encode("utf-8")
		if args.image:
			length = len(args.image)
			if length == 1:
				twitter.post.one_image(encoded, args.image)
			elif length >= 2 and length < 5:
				twitter.post.multi_images(encoded, args.image)
			elif length >= 5:
				printer.error("the maximium supported images are 4")
		elif args.url:
			if args.shortener:
				shortened_url = shortener.shorten_url(args.url, args.shortener)
			else:
				shortened_url = shortener.shorten_url(args.url, "tinyurl")
				twitter.post.text_only(encoded + "" + sortened_url)
		else:
			twitter.post.text_only(encoded)
	else:
		printer.error("please insert any argument (use -h if you need help)")

doallthings()
