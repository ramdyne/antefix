import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc):

    client.subscribe("/adsb/antefix/json")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    message = json.loads(msg.payload)
    if message['groundSpeed'] or message['callsign'] or message['lon']:
        output = "%s callsign %s, registration %s %s" % (message['operator'], message['callsign'], message['registration'], message['type'])
        if message['altitude'] :
            output = output + " altitude %d" % (message['altitude'])
        else :
            output = output + " altitude NaN"

        if message['lat'] and  message['lon'] :
            output = output + " @ (%f,%f)" % (message['lon'], message['lat'])

        print output

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

client.loop_forever()
