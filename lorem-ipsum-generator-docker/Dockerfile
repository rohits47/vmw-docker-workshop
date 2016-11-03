FROM nginx

RUN mkdir /etc/nginx/logs && touch /etc/nginx/logs/static.log

ADD nginx.conf /etc/nginx/conf.d/default.conf
ADD index.html /www/
ADD 404.html /www/
