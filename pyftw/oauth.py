#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# FTW
# OAuth module
#

import os
from .program import data
from twitter import *

app_name = data.app_name
key = data.key
key_secret = data.key_secret
creds_dir = os.path.expanduser("~/.ftw")
creds_file = "credentials"
twitter_creds = os.path.expanduser(creds_dir + "/" + creds_file)
if not os.path.exists(twitter_creds):
	if not os.path.exists(creds_dir):
		os.mkdir(creds_dir)
	oauth_dance(app_name, key, key_secret, twitter_creds)
token, token_key = read_token_file(twitter_creds)

class module:
	authorized = Twitter(auth=OAuth(token, token_key, key, key_secret))
