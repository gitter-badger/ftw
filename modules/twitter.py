#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Twitter module for Fast Tweet
#

import os
from twitter import *
from .echo import error, info

twitter_creds = os.path.expanduser("~/.ftw_credentials")
if not os.path.exists(twitter_creds):
    oauth_dance("Fast Tweet on Shell", "hQGQlPsTIN7iIsLVe6aHXycF0", "3vZ7Q1kPf3zkIBJEKxEL9FJr9WItEzmMz8ZjiU6Ozxm3tnSjJF", twitter_creds)

oauth_token, oauth_secret = read_token_file(twitter_creds)

twitter = Twitter(auth=OAuth(oauth_token, oauth_secret, "hQGQlPsTIN7iIsLVe6aHXycF0", "3vZ7Q1kPf3zkIBJEKxEL9FJr9WItEzmMz8ZjiU6Ozxm3tnSjJF"))

def check_chars(lenght):
    """
    Check the lenght of the tweet and if it have less of 'lenght' characters,
    send it, instead, raise a error througt echo.error() function.
    """
    check = lenght - 1
    if len(text) > check:
            error("Your tweet needs to be %s characters maximium!" % lenght, 1)

class post:
    def text_only(text):
        check_chars(140)
        info("Sending tweet: %s" % text)
        twitter.statuses.update(status=text)
        info("Sent sucessfully!")

    def with_image(text, image):
        check_chars(140)
        info("Adding image: %s" % image)
        with open(image, "rb") as image_file:
            image_data = image_file.read()
        upload_to = Twitter(domain="upload.twitter.com", auth=OAuth(token, token_key, con_secret, con_secret_key))
        image_id = upload_to.media.upload(media=image_data)["media_id_string"]
        info("Sending tweet: %s" % text)
        twitter.statuses.update(status=text, media_ids=",".join(image_id))
        info("Sent sucessfully!")
