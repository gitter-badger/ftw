#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# FTW 1.3
# Main script
#

import argparse
from pyftw import twitter, oauth, shortener, printer

app_name = "Fast Tweet on Shell"
version = "1.3"
codename = "Albatross"
key = "hQGQlPsTIN7iIsLVe6aHXycF0"
key_secret = "3vZ7Q1kPf3zkIBJEKxEL9FJr9WItEzmMz8ZjiU6Ozxm3tnSjJF"

parser = argparse.ArgumentParser(prog="ftw", description="terminal tweeting, ftw!")
parser.add_argument("text", type=str, nargs="?", help="tweet text")
parser.add_argument("-i", "--image", metavar="file", nargs="+", help="add one or more images")
parser.add_argument("-u", "--url", metavar="url", help="add a shortened url")
parser.add_argument("-s", "--shortener", metavar="shortener", default="tinyurl", help="change the shortener (defaults to tinyurl)")
parser.add_argument("-v", "--version", action="store_true", help="show version")

args = parser.parse_args()

creds_dir = os.path.expanduser("~/.ftw")
creds_file = "credentials"
twitter_creds = os.path.expanduser(creds_dir + "/" + creds_file)
if not os.path.exists(twitter_creds):
    if not os.path.exists(creds_dir):
        os.mkdir(creds_dir)
    oauth.authorize(key, key_secret)

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
