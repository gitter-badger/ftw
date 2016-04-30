#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# FTW 1.2
# Shortener functions
#

from .printer import info, error
from pyshorteners import Shortener

class utils:
    def shorten_url(service, url):
        if service == "google":
            shortener = Shortener("Google", api_key=api_key)
        elif service == "bitly":
            shortener = Shortener("Bitly", bitly_token=access_token)
        elif service == "owly":
            shortener = Shortener("Owly", api_key=api_key)
        else:
            shortener = Shortener("Tinyurl")
        shortened_url = shortener.short(url)
