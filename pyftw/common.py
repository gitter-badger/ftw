#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Common functions for Fast Tweet
#

def check_chars(text, lenght):
    if len(text) > lenght:
        error("your tweet needs to be %s characters maximium!" % lenght, 1)
    if len(text) == 0:
        error("please write something in your tweet", 1)
