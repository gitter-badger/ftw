#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Fast Tweet 1.1
#

import argparse
from pyftw import twitter, echo

version = "1.1"
codename = "Albatross"

parser = argparse.ArgumentParser(prog="ftw", description="terminal tweeting, ftw!")
parser.add_argument("text", type=str, nargs="?", help="tweet text")
parser.add_argument("-i", "--image", metavar="file", nargs="+", help="add one or more images")
parser.add_argument("-v", "--version", action="store_true", help="show version")

args = parser.parse_args()

if args.version:
    echo.version(version, codename)
else:
    encoded = args.text.encode("utf-8")
    if args.image:
    	length = len(arg.image)
    	if length == 1:
    		twitter.post.one_image(encoded, args.image)
    	elif length >= 2 and length < 5:
    		twitter.post.multi_images(encoded, args.image)
    else:
    	twitter.post.text_only(encoded)
