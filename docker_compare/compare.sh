for i in $(ls | grep Dockerfile.  ); do
    docker build -t fastapi_$(echo "$i" | cut -d"." -f2-) -f "$i" .
    ./docker_slim_tool/docker-slim build --target fastapi_$(echo "$i" | cut -d"." -f2-) --tag fastapi_docker_slim_$(echo "$i" | cut -d"." -f2-)

done

docker image ls -f 'reference=fastapi_*' --format "{{.Repository}}:{{.Tag}} {{.Size}}" | sort -k 2 -h
