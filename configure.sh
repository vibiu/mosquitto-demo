MOSQUITTO_VERSION="1.5.5"
MOSQUITTO_AUTH_PLUG_VERSION="0.1.3"
POSTGRES_VERSION="10.5"

echo mosquitto version is $MOSQUITTO_VERSION
echo postgres version is $POSTGRES_VERSION
echo mosquitto auth plug version is $MOSQUITTO_AUTH_PLUG_VERSION

mosquitto_dockerfile="mosquitto/Dockerfile"
postgres_dockerfile="postgres_db/Dockerfile"

sed -i "s/eclipse-mosquitto.*$/eclipse-mosquitto/" $mosquitto_dockerfile
sed -i "s/\<eclipse-mosquitto\>/&:"$MOSQUITTO_VERSION"/" $mosquitto_dockerfile

sed -i "s/ENV MOSQUITTO_AUTH_PLUG_VERSION.*$/ENV MOSQUITTO_AUTH_PLUG_VERSION/" $mosquitto_dockerfile
sed -i "s/\<ENV MOSQUITTO_AUTH_PLUG_VERSION\>/&="$MOSQUITTO_AUTH_PLUG_VERSION" MOSQUITO_VERSION="$MOSQUITTO_VERSION"/" $mosquitto_dockerfile

sed -i "s/postgres.*$/postgres/" $postgres_dockerfile
sed -i "s/\<postgres\>/&:"$POSTGRES_VERSION"/" $postgres_dockerfile

