#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# FTW 1.2
# Main script
#

import argparse
from pyftw import twitter, shortener, printer

version = "1.2"
codename = "Albatross"

parser = argparse.ArgumentParser(prog="ftw", description="terminal tweeting, ftw!")
parser.add_argument("text", type=str, nargs="?", help="tweet text")
parser.add_argument("-i", "--image", metavar="file", nargs="+", help="add one or more images")
parser.add_argument("-u", "--url", metavar="url", help="add a shortened url")
parser.add_argument("-s", "--shortener", metavar="shortener", default="tinyurl", help="change the shortener (defaults to tinyurl)")
parser.add_argument("-v", "--version", action="store_true", help="show version")

args = parser.parse_args()

if args.version:
    printer.version(version, codename)
else:
    encoded = args.text.encode("utf-8")
    if args.image:
        length = len(args.image)
        if length == 1:
            twitter.post.one_image(encoded, args.image)
        elif length >= 2 and length < 5:
            twitter.post.multi_images(encoded, args.image)
        elif length >= 5:
            printer.error("the maximium supported images are 4!", 1)
    else:
      if args.url:
        if args.shortener:
          shortened_url = shortener.shorten_url(args.url, args.shortener)
        else:
          shortened_url = shortener.shorten_url(args.url, "tinyurl")
          twitter.post.text_only(encoded + "" + sortened_url)
      else:
        twitter.post.text_only(encoded)
