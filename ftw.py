#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Fast Tweet 1.0.1
#

import argparse
from fastw import twitter
from fastw import echo

version = "1.0.1"
codename = "Budgie"

parser = argparse.ArgumentParser(prog="ftw", description="terminal tweeting, ftw!", usage="%(prog)s \"text\" [--image file]")
parser.add_argument("text", type=str, nargs="?", help="tweet text")
parser.add_argument("--image", metavar="file", help="add a image")
parser.add_argument("--version", action="store_true", help="show version")

args = parser.parse_args()

if args.version:
    echo.version(version, codename)
else:
    if args.image:
        twitter.post.with_image(args.text, args.image)
    else:
        twitter.post.text_only(args.text)
