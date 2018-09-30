import paho.mqtt.publish as publish
import time

HOST = 'mosquitto'
PORT = 1883


if __name__ == '__main__':
    client_id = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    publish.single('/p/vibiu/mytopic', 'hello mqtt', qos=2, hostname=HOST, port=PORT,
        client_id=client_id, auth={'username': 'vibiu', 'password': '123456'})

