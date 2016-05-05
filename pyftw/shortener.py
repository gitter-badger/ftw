#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# FTW 1.3
# Shortener functions
#

from pyshorteners import Shortener

def shorten_url(url, service):
  if service == "google":
    shortener = Shortener("Google", api_key=api_key)
  elif service == "bitly":
    shortener = Shortener("Bitly", bitly_token=access_token)
  elif service == "owly":
    shortener = Shortener("Owly", api_key=api_key)
  elif service == "tinyurl":
    shortener = Shortener("Tinyurl")
  shortened_url = shortener.short(url)
  return shortened_url
