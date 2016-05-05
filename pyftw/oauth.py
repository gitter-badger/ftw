#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# FTW 1.3
# OAuth functions
#

def authorize(app_name, key, key_secret):
	oauth_dance(app_name, key, key_secret, twitter_creds)
	token, token_key = read_token_file(twitter_creds)
	twitter = Twitter(auth=OAuth(token, token_key, key, key_secret))
