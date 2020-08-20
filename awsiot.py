import paho.mqtt.client as pub
import time

c = pub.Client("iotconsole-1597901323631-2")
c.tls_set("certificates/AmazonRootCA1.crt",certfile ="certificates/b5f060950a_certificate.pem", keyfile = "certificates/b5f060950a_private.pem")
c.connect("a161gataej7hrq-ats.iot.ap-south-1.amazonaws.com", 8883, 45)
count = 0
time.sleep(1)
c.publish("myTopic", "hi", qos = 1)
count = count + 1
print(count)
    
