import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time

HOST = 'mosquitto'
PORT = 1883

def client_loop():
    client_id = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    client = mqtt.Client(
        client_id=client_id, clean_session=True)
    client.username_pw_set('client', '123456')
    client.on_connect = on_connect 
    client.on_message = on_message
    client.connect(HOST, PORT, 60)
    client.loop_forever()


def on_connect(client, userdata, flags, rc):
    print('Connected with result code ' + str(rc))
    # client.subscribe('/p/vibiu/mytopic')
    client.subscribe('/p/client/upload')


def on_message(client, userdata, msg):
    print(msg.topic + ' ' + msg.payload.decode('utf-8'))


if __name__ == '__main__':
    client_loop()
    
