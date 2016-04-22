#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Fast Tweet 1.0.1
#

import argparse
from fastw import twitter, echo

version = "1.0.1"
codename = "Budgie"

parser = argparse.ArgumentParser(prog="ftw", description="terminal tweeting, ftw!")
parser.add_argument("text", type=str, nargs="?", help="tweet text")
parser.add_argument("-i", "--image", metavar="file", nargs="*", help="add one or more images")
parser.add_argument("-v", "--version", action="store_true", help="show version")

args = parser.parse_args()

if args.version:
    echo.version(version, codename)
else:
    args.text = args.text.encode("utf-8")
    if args.image:
       twitter.post.with_images(args.text, args.image)
    else:
       twitter.post.text_only(args.text)
