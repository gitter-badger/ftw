#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Poster! v0.0.1-Alpha0
#

import argparse
from modules import twitter

parser = argparse.ArgumentParser(description="Send a message, anywhere!")
parser.add_argument("--version", "-v", action="store_true", help="Poster! version")
parser.add_argument("--tweet", "-tw", type=str, help="Send a tweet")
parser.add_argument("--image", help="Add a image to your tweet")
args = parser.parse_args()

version = "0.0.1-Alpha0"
codename = "Rose"

if args.version:
    print("Version: %s \"%s\"" % (version, codename))
elif args.tweet:
    if args.image:
        twitter.send(args.tweet, args.image)
    else:
        twitter.send(args.tweet)
