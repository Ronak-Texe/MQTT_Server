import paho.mqtt.client as mqtt
import Control_Panel

def on_connect(client, userdata, flags, rc):
    print('Connected with MQTT Server')
    client.subscribe('sensordata1')
    client.subscribe('sensordata2')

def on_message(client, userdata, msg):
    
    post_data=(msg.payload).decode()
    if(msg.topic=='sensordata1'):
        Control_Panel.ControlPanel1(post_data)
        
    elif(msg.topic=='sensordata2'):
        Control_Panel.ControlPanel2(post_data)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect('52.56.146.236', 1883, 60)
client.loop_forever()