#!/bin/bash

NGINX_PORT="1080"
docker build -t teachpyby.github.io:latest .
echo ""
echo "> Open http://localhost:$NGINX_PORT/ "
echo ""
echo ""
docker run -v "$(pwd):/var/www/data" -p$NGINX_PORT:80 teachpyby.github.io:latest
