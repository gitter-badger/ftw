#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Poster! v0.0.1-Alpha0
#

import argparse
from modules import twitter

parser = argparse.ArgumentParser(description="Send a message, anywhere!")
parser.add_argument("--twitter-status", "-ts", type=str, help="Send a tweet")
args = parser.parse_args()

if args.twitter_status:
    twitter.send(args.twitter_status)
