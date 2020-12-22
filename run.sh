#!/bin/bash

docker build -t teachpyby.github.io:latest .
docker run -v "$(pwd):/var/www/data" -p1080:1080 teachpyby.github.io:latest
