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

token, token_key = read_token_file(twitter_creds)

twitter = Twitter(auth=OAuth(token, token_key, "hQGQlPsTIN7iIsLVe6aHXycF0", "3vZ7Q1kPf3zkIBJEKxEL9FJr9WItEzmMz8ZjiU6Ozxm3tnSjJF"))

def check_chars(text, lenght):
    if len(text) > lenght:
        error("your tweet needs to be %s characters maximium!" % lenght, 1)
    if len(text) == 0:
        error("please write something in your tweet", 1)

def check_images(images, number):
    if len(images) == number:
        error("maximium images: %s!" % number, 1)

class post:
    def text_only(text):
        check_chars(text, 140)
        info("sending tweet: %s" % text)
        twitter.statuses.update(status=text)
        info("sent sucessfully!")

    def with_images(text, images):
        check_chars(text, 140)
        check_images(images, 4)
        info("adding images: %s" % images)
        if len(images) == 1:
            image = images[0]
            with open(image, "rb") as image_file:
                image_data = image_file.read()
            upload_to = Twitter(domain="upload.twitter.com", auth=OAuth(token, token_key, "hQGQlPsTIN7iIsLVe6aHXycF0", "3vZ7Q1kPf3zkIBJEKxEL9FJr9WItEzmMz8ZjiU6Ozxm3tnSjJF"))
            image_id = upload_to.media.upload(media=image_data)["media_id_string"]
            info("sending tweet: %s" % text)
            twitter.statuses.update(status=text, media_ids=",".join([image_id]))
            info("sent sucessfully!")
        else:
            for image in images:
                joiners = []
                with open(image, "rb") as image_file:
                    image_data = image_file.read()
                upload_to = Twitter(domain="upload.twitter.com", auth=OAuth(token, token_key, "hQGQlPsTIN7iIsLVe6aHXycF0", "3vZ7Q1kPf3zkIBJEKxEL9FJr9WItEzmMz8ZjiU6Ozxm3tnSjJF"))
                image_id = upload_to.media.upload(media=image_data)["media_id_string"]
                joiners.append(image_id) 
            info("sending tweet: %s" % text)
            twitter.statuses.update(status=text, media_ids=",".join(joiners))
            info("sent sucessfully!")
