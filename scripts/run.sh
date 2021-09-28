#!/bin/bash

PORT="1080"
echo ""
echo "> Open http://localhost:$PORT/ "
echo ""
echo ""
python -m http.server $PORT --bind localhost --directory $(pwd)
