FROM postgres:latest
ENV POSTGRES_DB=mosquitto POSTGRES_USER=root POSTGRES_PASSWORD=root_password
ADD ./init.sh /docker-entrypoint-initdb.d/init.sh

