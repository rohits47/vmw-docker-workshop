docker stop flaskapp
docker rm flaskapp
docker run --name flaskapp \
    -p 80:80 \
    -v `pwd`/backend/:/app \
    -d jazzdd/alpine-flask -d
