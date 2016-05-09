#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# FTW
# Twitter module
#

from .common import printer, checks
from .oauth import module
from twitter import *
from pyshorteners import Shortener

twitter = api.authenticated

class shortener:
	def make_short(url, service):
		if service == "google":
			shortener = Shortener("Google", api_key=api_key)
		elif service == "bitly":
			shortener = Shortener("Bitly", bitly_token=access_token)
		elif service == "owly":
			shortener = Shortener("Owly", api_key=api_key)
		elif service == "tinyurl":
			shortener = Shortener("Tinyurl")
		new_url = shortener.short(url)
		return new_url

class post:
	def text_only(text):
		max_chars(text, 140)
		printer.info("sending tweet: {}".format(text))
		twitter.statuses.update(status=text)
		printer.info("sent sucessfully!")

	def one_image(text, image):
		max_chars(text, 140)
		printer.info("sending tweet: {}".format(text))
		printer.info("adding image: {}".format(image))
		with open(image[0], "rb") as image_file:
			image_data = image_file.read()
		upload_to = Twitter(domain="upload.twitter.com", auth=OAuth(token, token_key, key, key_secret))
		image_id = upload_to.media.upload(media=image_data)["media_id_string"]
		twitter.statuses.update(status=text, media_ids=image_id)
		printer.info("sent sucessfully!")

	def multi_images(text, images):
		max_chars(text, 140)
		printer.info("sending tweet: {}".format(text))
		printer.info("adding images: {}".format(images))
		image_ids = []
		# Ugly hack
		if len(images) >= 1:
			with open(images[0], "rb") as image_file:
				image_data = image_file.read()
			upload_to = Twitter(domain="upload.twitter.com", auth=OAuth(token, token_key, key, key_secret))
			image_id_1 = upload_to.media.upload(media=image_data)["media_id_string"]
			image_ids.append(image_id_1)
		if len(images) >= 2:
			with open(images[1], "rb") as image_file:
				image_data = image_file.read()
			upload_to = Twitter(domain="upload.twitter.com", auth=OAuth(token, token_key, key, key_secret))
			image_id_2 = upload_to.media.upload(media=image_data)["media_id_string"]
			image_ids.append(image_id_2)
		if len(images) >= 3:
			with open(images[2], "rb") as image_file:
				image_data = image_file.read()
			upload_to = Twitter(domain="upload.twitter.com", auth=OAuth(token, token_key, key, key_secret))
			image_id_3 = upload_to.media.upload(media=image_data)["media_id_string"]
			image_ids.append(image_id_3)
		if len(images) == 4:
			with open(images[3], "rb") as image_file:
				image_data = image_file.read()
			upload_to = Twitter(domain="upload.twitter.com", auth=OAuth(token, token_key, key, key_secret))
			image_id_4 = upload_to.media.upload(media=image_data)["media_id_string"]
			image_ids.append(image_id_4)
		twitter.statuses.update(status=text, media_ids=",".join(image_ids))
		printer.info("sent sucessfully!")
