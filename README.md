# Mosquitto docker-compose demo
This is a demo of mosquitto with mosquitto-auth-plug.

Source code is based on [eclipse/mosquitto](https://github.com/eclipse/mosquitto) and [jpmens/mosquitto](https://github.com/jpmens/mosquitto-auth-plug).

Mosquitto image is based on [dockerhub/eclipse-mosquitto](https://hub.docker.com/_/eclipse-mosquitto).

Postgres image is based on [dockerhub/postgres](https://hub.docker.com/_/postgres).

current version:
* mosquitto:1.5.5
* mosquitto-auth-plug:0.1.2
* potgres:10.5

# Run it with docker-compose
Docker:18.06.1-ce is tested, other docker version should work in theroy.

Docker-compose:1.22.0 is tested, other docker-compose which support docker-compose.yml version 3 will work.

## build images
```
docker-compose build
```
if you want to build without cache:
```
docker-compose build --no-cache
```

## run containers
```
docker-compose up -d
```
some times the mosquitto container will not work just because the healthcheck is not pass. It's strange, but you can run this code again.

# Try other mosquitto version
Edit `configure.sh`, change the version here if you like.
```
MOSQUITTO_VERSION="1.5.5"
MOSQUITTO_AUTH_PLUG_VERSION="0.1.2"
POSTGRES_VERSION="10.5"
```
then execute:
```
sh ./configre.sh
```
build your docker images again after that.

# Customize mosquitto config
Edit `mosquitto/config/config.mk` and `mosquitto/config/mosquitto.conf`.

You can read more about the usage of thease two file in [jpmens/mosquitto-auth-plug/README.md](https://github.com/jpmens/mosquitto-auth-plug/blob/master/README.md)


