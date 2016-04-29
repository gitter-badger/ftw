#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Twitter module for Fast Tweet
#

import os
from twitter import *
from .echo import error, info
from .common import check_chars

key = "hQGQlPsTIN7iIsLVe6aHXycF0"
key_secret = "3vZ7Q1kPf3zkIBJEKxEL9FJr9WItEzmMz8ZjiU6Ozxm3tnSjJF"

twitter_creds = os.path.expanduser("~/.ftw_auth")
if not os.path.exists(twitter_creds):
    oauth_dance("Fast Tweet on Shell", key, key_secret, twitter_creds)

token, token_key = read_token_file(twitter_creds)

twitter = Twitter(auth=OAuth(token, token_key, key, key_secret))

class post:
    def text_only(text):
        check_chars(text, 140)
        info("sending tweet: %s" % text)
        twitter.statuses.update(status=text)
        info("sent sucessfully!")

    def one_image(text, image):
        check_chars(text, 140)
        info("sending tweet: %s" % text)
        info("adding image: %s" % image)
        image = images[0]
        with open(image, "rb") as image_file:
            image_data = image_file.read()
        upload_to = Twitter(domain="upload.twitter.com", auth=OAuth(token, token_key, key, key_secret))
        image_id = upload_to.media.upload(media=image_data)["media_id_string"]
        twitter.statuses.update(status=text, media_ids=",".join([image_id]))
        info("sent sucessfully!")

    def multi_images(text, images):
        check_chars(text, 140)
        info("sending tweet: %s" % text)
        info("adding images: %s" % images)
        if len(images) == number:
            error("maximium images: %s!" % number, 1)
        for image in images:
            with open(image, "rb") as image_file:
                image_data = image_file.read()
            upload_to = Twitter(domain="upload.twitter.com", auth=OAuth(token, token_key, key, key_secret))
            image_id = upload_to.media.upload(media=image_data)["media_id_string"]
        twitter.statuses.update(status=text, media_ids=",".join(image_id))
        info("sent sucessfully!")
