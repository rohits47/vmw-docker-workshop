docker stop flaskapp
docker rm flaskapp
docker exec flaskapp /bin/bash -c "pip install twitter"
docker run --name flaskapp \
    -p 80:80 \
    -v `pwd`/backend/:/app \
    -d jazzdd/alpine-flask
