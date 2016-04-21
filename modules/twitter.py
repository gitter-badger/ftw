#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Twitter module for Poster!
#

import os
from twitter import *
from .echo import error, info

twitter_creds = os.path.expanduser("~/.poster_twitter")
if not os.path.exists(twitter_creds):
    oauth_dance("Poster!", "hQGQlPsTIN7iIsLVe6aHXycF0", "3vZ7Q1kPf3zkIBJEKxEL9FJr9WItEzmMz8ZjiU6Ozxm3tnSjJF", twitter_creds)

oauth_token, oauth_secret = read_token_file(twitter_creds)

twitter = Twitter(auth=OAuth(oauth_token, oauth_secret, "hQGQlPsTIN7iIsLVe6aHXycF0", "3vZ7Q1kPf3zkIBJEKxEL9FJr9WItEzmMz8ZjiU6Ozxm3tnSjJF"))

def post(tweet_text, *image):
    """
    Check the lenght of the tweet and if it have less of 140 characters,
    send it, instead, raise a error througt echo.error() function.
    """
    if len(tweet_text) > 139:
        error("Your tweet needs to be 140 characters maximium!", 1)
    else:
        info("Sending tweet: %s" % tweet_text)
        if image:
            info("Adding image: %s" % image)
            with open(image, "rb") as image_file:
                image_data = image_file.read()
            upload_to = Twitter(domain="upload.twitter.com", auth=OAuth(token, token_key, con_secret, con_secret_key))
            image_id = upload_to.media.upload(media=image_data)["media_id_string"]
            twitter.statuses.update(status=tweet_text, media_ids=",".join(image_id))
        else:
            twitter.statuses.update(status=tweet_text)
        info("Sent sucessfully!")
