#!/bin/bash
# takes a URL, sends request and displays size of the response
curl -sI "$1" | grep 'Content-Length:' | cut -d' ' -f2
