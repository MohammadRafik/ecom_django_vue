FROM python:3.7.9-buster

RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
COPY letsencrypt /etc/letsencrypt
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log
COPY requirements.txt start-server.sh /usr/src/app/
RUN mkdir -p /usr/src/app/src
COPY src /usr/src/app/src
WORKDIR /usr/src/app
RUN pip install -r requirements.txt
RUN chown -R www-data:www-data /usr/src/app
EXPOSE 80 443
STOPSIGNAL SIGTERM
CMD ["/usr/src/app/start-server.sh"]


