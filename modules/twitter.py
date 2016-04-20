#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Twitter module for Poster!
#

from TwitterAPI import TwitterAPI
from .echo import error, info

api = TwitterAPI("hQGQlPsTIN7iIsLVe6aHXycF0",
                 "3vZ7Q1kPf3zkIBJEKxEL9FJr9WItEzmMz8ZjiU6Ozxm3tnSjJF",
                 "2318747108-UV0gtMlxxoEybK8EkMCmzkIZ8mmNP4ER4Blnlor", # Only me can use it, by now...
                 "926khkT44bHsXpqQI6SuwhGqTSyWMK9WwV2pvi3tMNMku"       # check "da great TODO" on README.md
                )

def send(tweet_text):
    """
    Check the lenght of the tweet and if it have less of 140 characters,
    send it, instead, raise a error througt echo.error() function.
    """
    if len(tweet_text) > 139:
        error("Your tweet needs to be 140 characters maximium!", 1)

    # Da Status sending magic
    tweet = api.request("statuses/update", {"status": tweet_text})

    """
    If the sent was sucessfully (twitter.status_code = 200), print a
    message, instead, raise a error with the obtained status_code.
    """
    info("Sending tweet: %s" % tweet_text)

    if tweet.status_code == 200:
        info("Sent sucessfully!")
    else:
        error("Failed to sent tweet! Obtained status %s" % tweet.status_code, 1)
