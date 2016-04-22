#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Print function modifications for Fast Tweet
#

import sys

class color:
    none = "\033[0m"
    bold = "\033[1m"
    red = "\033[91m"
    green = "\033[92m"
    yellow = "\033[93m"

def info(msg):
    print(color.green + "[info] %s" % msg + color.none)

def error(msg, code):
    print(color.red + "[error] %s" % msg + color.none)
    print(color.red + "[error] exiting with code %i" % code + color.none)
    sys.exit(code)

def warning(msg):
    print(color.yellow + "[warning] %s" % msg + color.none)

def version(ver, name):
    print("version: %s \"%s\"" % (ver, name))
    sys.exit(0)
