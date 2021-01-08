# Quickstart Fastapi (245 MB)

## Build container
docker build -t small_fast_api . 

## Run container
docker run -p 80:80 -it small_fast_api

## delete container
docker kill $(docker ps -a -q)

## in one line
docker kill $(docker ps -a -q) && docker build -t small_fast_api . && docker run -p 80:80 -it small_fast_api