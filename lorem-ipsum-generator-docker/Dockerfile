FROM nginx

RUN mkdir /etc/nginx/logs && touch /etc/nginx/logs/static.log

ADD nginx.conf /etc/nginx/conf.d/default.conf
ADD frontend/index.html /www/
ADD frontend/grid.css /www/
ADD parse_json.py /www/
ADD sample_input.json /www/
#ADD frontend/dist/ /www/
#ADD frontend/assets/ /www/
ADD 404.html /www/
ADD frontend/background_bird.png /www/
