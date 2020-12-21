#!/bin/bash

docker build -t teachpyby.github.io:latest .
docker run -v "$(pwd):/var/www/data" -p80:80 teachpyby.github.io:latest
