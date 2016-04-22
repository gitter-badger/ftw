#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Fast Tweet 1.0 
#

import argparse
from modules import twitter, echo

version = 1.0
codename = "Albatross"

parser = argparse.ArgumentParser(prog="ftw", description="terminal tweeting, FTW!", usage="%(prog)s \"text\" [--image file]")
parser.add_argument("text", type=str, nargs="?", help="tweet text")
parser.add_argument("--image", metavar="file", help="add a image")
parser.add_argument("--version", action="store_true", help="Fast Tweet version")

args = parser.parse_args()

if args.version:
    echo.version(version, codename)
else:
    if args.image:
        twitter.post.with_image(args.text, args.image)
    else:
        twitter.post.text_only(args.text)
