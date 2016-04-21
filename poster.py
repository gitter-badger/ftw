#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Poster v0.0.1-Alpha0
#

import argparse
from modules import twitter
from modules.echo import info

version = "0.0.1-Alpha0"
codename = "Rose"

parser = argparse.ArgumentParser(prog="poster", description="Send a message, anywhere!",
                                 usage="%(prog)s -tw \"TEXT\" [--image FILE]")
parser.add_argument("-v", "--version",
                    action="store_true", help="Poster version")
parser.add_argument("-tw", "--tweet", type=str, metavar="\"TEXT\"", help="Send a tweet")
parser.add_argument("--image", metavar="FILE", help="Add a image to your tweet")

args = parser.parse_args()

if args.version:
    info("Version: %s \"%s\"" % (version, codename))
elif args.tweet:
    if args.image:
        twitter.post(args.tweet, args.image)
    else:
        twitter.post(args.tweet)
