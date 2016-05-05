#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# FTW 1.3
# OAuth functions
#

import os
from twitter import *

class auth:
    def orize(app_name, key, key_secret):
        creds_dir = os.path.expanduser("~/.ftw")
        creds_file = "credentials"
        twitter_creds = os.path.expanduser(creds_dir + "/" + creds_file)
        if not os.path.exists(twitter_creds):
            if not os.path.exists(creds_dir):
                os.mkdir(creds_dir)
            oauth_dance(app_name, key, key_secret, twitter_creds)
            token, token_key = read_token_file(twitter_creds)
    twitter = Twitter(auth=OAuth(token, token_key, key, key_secret))
