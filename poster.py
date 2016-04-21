#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Poster! v0.0.1-Alpha0
#

import argparse
from modules import twitter

parser = argparse.ArgumentParser(description="Send a message, anywhere!")
parser.add_argument("--tweet", "-tw", type=str, help="Send a tweet")
args = parser.parse_args()

if args.tweet:
    twitter.send(args.tweet)
