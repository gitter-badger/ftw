#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Twitter module for Poster!
#

import os
import twitter
from .echo import error, info


twitter_creds = os.path.expanduser('~/.poster_twitter')
if not os.path.exists(twitter_creds):
    twitter.oauth_dance("Poster!", "hQGQlPsTIN7iIsLVe6aHXycF0", "3vZ7Q1kPf3zkIBJEKxEL9FJr9WItEzmMz8ZjiU6Ozxm3tnSjJF", twitter_creds)

oauth_token, oauth_secret = twitter.read_token_file(twitter_creds)

twitter = twitter.Twitter(auth=twitter.OAuth(oauth_token, oauth_secret, "hQGQlPsTIN7iIsLVe6aHXycF0", "3vZ7Q1kPf3zkIBJEKxEL9FJr9WItEzmMz8ZjiU6Ozxm3tnSjJF"))

def send(tweet_text):
    """
    Check the lenght of the tweet and if it have less of 140 characters,
    send it, instead, raise a error througt echo.error() function.
    """
    if len(tweet_text) > 139:
        error("Your tweet needs to be 140 characters maximium!", 1)

    # Da Status sending magic
    twitter.statuses.update(status=tweet_text)

    """
    If the sent was sucessfully (twitter.status_code = 200), print a
    message, instead, raise a error with the obtained status_code.
    """
    info("Sending tweet: %s" % tweet_text)
    info("Sent sucessfully!")
