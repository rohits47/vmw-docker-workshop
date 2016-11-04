docker stop customflaskapp
docker rm customflaskapp
#docker build -t customflaskapp .
docker run --name customflaskapp \
    -p 80:80 \
    -v `pwd`/backend/:/app \
    -d customflaskapp
