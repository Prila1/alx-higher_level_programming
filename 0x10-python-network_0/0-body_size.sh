#!/bin/bash
#Showss the body size of a response

curl -s -w "%{size_download}\n" -o /dev/null "$1"
