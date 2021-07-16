FROM ubuntu:latest

USER root

RUN apt-get update && apt-get install -y supervisor
RUN mkdir -p /var/log/supervisor
COPY ./config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN apt-get install -y python3 python3-pip python3-dev build-essential
RUN ln -s /usr/bin/python3 /usr/bin/python

RUN mkdir -p /app
COPY ./src /app

EXPOSE 23233
CMD ["/usr/bin/supervisord"]
