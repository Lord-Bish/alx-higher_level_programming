#!/bin/bash
# sends a DELETE request to the URL's first argument and displays response of body
curl -sX DELETE "$1"
