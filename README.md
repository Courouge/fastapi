
docker rm $(docker stop $(docker ps -a -q --filter name="myfastcontainer" --format="{{.ID}}"))

docker build -t myfastapi:"$(<.version)" . && docker run -d --name myfastcontainer -p 80:80  myfastapi:"$(<.version)"

docker-compose exec web pytest .


## fast way ##
## delete and recreate
docker rm $(docker stop $(docker ps -a -q --filter name="myfastcontainer" --format="{{.ID}}")) && docker build -t myfastapi:"$(<.version)" . && docker run -d --name myfastcontainer -p 80:80  myfastapi:"$(<.version)"

## build and test
docker-compose up -d --build && docker-compose exec web pytest .

## connect to container
docker-compose exec web sh