FROM eclipse-mosquitto
WORKDIR /mosquitto
ADD src /mosquitto/src
ADD config /mosquitto/config
ADD docker-entrypoint.sh /docker-entrypoint.sh

RUN echo "http://mirrors.aliyun.com/alpine/v3.4/main/" > /etc/apk/repositories && \
    apk update && \
    apk add git && \ 
    apk add mosquitto-dev && \
    apk add postgresql-dev && \
    apk add openssl && \
    apk add build-base && \
    echo "192.30.253.112     github.com" >> /etc/hosts && \
    echo "151.101.72.133    assets-cdn.github.com" >> /etc/hosts && \
    echo "151.101.193.194    github.global.ssl.fastly.net" >> /etc/hosts && \
    git clone https://github.com/eclipse/mosquitto /mosquitto/src/mosquitto && \
    git clone https://github.com/jpmens/mosquitto-auth-plug /mosquitto/src/mosquitto-auth-plug && \
    mv /mosquitto/config/config.mk /mosquitto/src/mosquitto-auth-plug/config.mk &&\
    cd /mosquitto/src/mosquitto-auth-plug && \
    make clean && make

EXPOSE 1881 9001

