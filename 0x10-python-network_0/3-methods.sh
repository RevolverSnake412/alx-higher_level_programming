#!/bin/bash
# Displays all allowed methods
curl -sI $1 | grep Allow: | awk -F ': ' '{print $2}'
