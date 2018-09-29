FROM eclipse-mosquitto
WORKDIR /mosquitto
ADD config /mosquitto/config
COPY ./docker-entrypoint.sh /

RUN echo "http://mirrors.aliyun.com/alpine/v3.4/main/" > /etc/apk/repositories && \
    apk update && \
    apk add git && \ 
    apk add mosquitto-dev && \
    apk add postgresql-dev && \
    apk add openssl && \
    apk add build-base && \
    git clone https://github.com/eclipse/mosquitto /mosquitto/src/mosquitto && \
    git clone https://github.com/jpmens/mosquitto-auth-plug /mosquitto/src/mosquitto-auth-plug &&\
    mv /mosquitto/config/config.mk /mosquitto/src/mosquitto-auth-plug/config.mk &&\
    cd /mosquitto/src/mosquitto-auth-plug && \
    make clean && make

EXPOSE 1881 9001

