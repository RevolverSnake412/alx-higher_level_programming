#!/bin/bash
# Sends parameter to the provided URL
curl -sX POST $1 -d "email=test@gmail.com&subject=I will always be here for PLD"
