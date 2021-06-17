# Quickstart Docker Fastapi
This project aim to compare dockerfile and docker-slim equivalent.

In my case, I try to find the smallest docker image :)

# Execute build & compare images
`./compare.sh`

```
fastapi_sl_tiangolo_slim_distroless   latest    06b7e87c440f   1 second ago         25.1MB
fastapi_sl_tiangolo_slim              latest    c21c4942b793   27 seconds ago       125MB
fastapi_sl_tiangolo_alpine            latest    d5f75e683039   About a minute ago   22.4MB
fastapi_sl_slim_distroless            latest    49e0e2aca268   About a minute ago   25.2MB
fastapi_sl_debian_distroless          latest    053c352a1974   2 minutes ago        56.3MB
fastapi_sl_alpine_distroless          latest    c692cc10ed71   2 minutes ago        25.4MB
fastapi_tiangolo_slim_distroless      latest    f3ca1e37bcc0   19 minutes ago       149MB
fastapi_tiangolo_alpine               latest    e2641767a5d1   7 hours ago          102MB
fastapi_slim_distroless               latest    4f8a2d8fc7e4   7 hours ago          101MB
fastapi_tiangolo_slim                 latest    4c5a64506b29   7 hours ago          243MB
fastapi_alpine_distroless             latest    3a5f4c829ba4   25 hours ago         55.3MB
fastapi_debian_distroless             latest    13876126c659   2 days ago           104MB

```
