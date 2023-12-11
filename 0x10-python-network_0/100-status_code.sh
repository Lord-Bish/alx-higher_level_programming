#!/bin/bash
# sends a request to URL and displays status code of the response
curl -so /dev/null --write-out "%{http_code}" "$1"
