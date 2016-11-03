docker stop lorem-ipsum
docker rm lorem-ipsum
docker build -t lorem-ipsum .
docker run -p 80:80 -d --name lorem-ipsum lorem-ipsum
