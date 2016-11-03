FROM nginx

RUN mkdir /etc/nginx/logs && touch /etc/nginx/logs/static.log

ADD nginx.conf /etc/nginx/conf.d/default.conf
ADD frontend/index.html /www/
ADD frontend/grid.css /www/
ADD frontend/dist/ /www/
ADD frontend/assets/ /www/
ADD 404.html /www/
