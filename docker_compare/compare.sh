docker build -t fastapi_alpine_distroless -f Dockerfile.apline_distroless . && \
docker build -t fastapi_debian_distroless -f Dockerfile.debian_distroless . && \
docker build -t fastapi_slim_distroless -f Dockerfile.slim_distroless . && \
docker build -t fastapi_tiangolo_alpine -f Dockerfile.tiangolo_alpine . && \
docker build -t fastapi_tiangolo_slim -f Dockerfile.tiangolo_slim . && \
docker build -t fastapi_tiangolo_slim_distroless -f Dockerfile.tiangolo_slim_distroless . && \

./docker_slim_tool/docker-slim build --target fastapi_alpine_distroless --tag fastapi_sl_alpine_distroless  && \
./docker_slim_tool/docker-slim build --target fastapi_debian_distroless --tag fastapi_sl_debian_distroless  && \
./docker_slim_tool/docker-slim build --target fastapi_slim_distroless --tag fastapi_sl_slim_distroless  && \
./docker_slim_tool/docker-slim build --target fastapi_tiangolo_alpine --tag fastapi_sl_tiangolo_alpine  && \
./docker_slim_tool/docker-slim build --target fastapi_tiangolo_slim --tag fastapi_sl_tiangolo_slim  && \
./docker_slim_tool/docker-slim build --target fastapi_tiangolo_slim_distroless --tag fastapi_sl_tiangolo_slim_distroless  && \

docker image ls -f 'reference=fastapi_*'
