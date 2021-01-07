import paho.mqtt.client as mqtt
broker_address="18.229.149.156"
#generar cliente
client= mqtt.Client("Pablo")
#conectar a servidor
client.connect(broker_address,port=1883)

#una vez conectado, enviar mensajes
client.publish("temperatura","")


