#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Print function modifications for Poster
#

import sys

class color:
    none = "\033[0m"
    bold = "\033[1m"
    red = "\033[91m"
    green = "\033[92m"
    yellow = "\033[93m"

def info(message):
    print(color.green + "[INFO]: %s" % message + color.none)

def error(message, code):
    print(color.red + "[ERROR]: %s" % message + color.none)
    print(color.red + "[ERROR]: Exiting with code %i" % code + color.none)
    sys.exit(code)

def warning(message):
    print(color.yellow + "[WARNING]: %s" + color.none % message)
