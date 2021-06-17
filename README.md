# Quickstart Docker Fastapi
This project aim to compare dockerfile and docker-slim equivalent.

In my case, I try to find the smallest docker image :)

# Execute build & compare images
`./compare.sh`

fastapi_sl_tiangolo_slim       latest    7691581e0550   1 second ago         125MB

fastapi_sl_tiangolo_alpine     latest    0d03fc853983   45 seconds ago       22.4MB

fastapi_sl_slim_distroless     latest    2d6813ba6e41   About a minute ago   25MB

fastapi_sl_debian_distroless   latest    421dd265b356   About a minute ago   56.6MB

fastapi_sl_alpine_distroless   latest    af31ef21827e   2 minutes ago        25.5MB

fastapi_tiangolo_alpine        latest    e2641767a5d1   6 minutes ago        102MB

fastapi_slim_distroless        latest    4f8a2d8fc7e4   6 minutes ago        101MB

fastapi_tiangolo_slim          latest    4c5a64506b29   14 minutes ago       243MB

fastapi_alpine_distroless      latest    3a5f4c829ba4   18 hours ago         55.3MB

fastapi_debian_distroless      latest    13876126c659   2 days ago           104MB
