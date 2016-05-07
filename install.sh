#!/usr/bin/env bash
#
# FTW
# Install script
#

case $1 in
	"build") make clean; make build;;
	"uninstall") make clean-root;;
	"") make clean-root; make install;;
	*) echo "Unexpected input!"; exit 1;;
esac
