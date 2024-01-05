#!/bin/bash
# Displays the content length of an URL
curl -sI $1 | grep Content-Length: | awk '{print $2}'
