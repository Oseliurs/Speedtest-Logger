## Import
import speedtest
import paho.mqtt.client as mqtt

## Paramètres
servers = []
# If you want to test against a specific server

threads = None
# If you want to use a single threaded test

test = True
# If you want to do the speedtest or just test the rest of the code

# Connect to MQTT Broker
client = mqtt.Client()
username_pw_set(user, password="Ov96Hf66&*")
client.connect("rutaceae.ddns.net", 1883)

## Code
if test == True:
  # Do a speedtest.
  print("Warning Speedtesting: You may encounter some slowlyness while the test is running.")
  s = speedtest.Speedtest()
  s.get_servers(servers)
  s.get_best_server()
  s.download(threads=threads)
  s.upload(threads=threads)
  print("Speedtest Done !!!")
  s.results.share()
  results_dict = s.results.dict()

# print(results_dict)

# print([ strftime("%H:%M:%S", gmtime()), strftime("%x"), results_dict["ping"], results_dict["download"]/1000000, results_dict["upload"]/1000000 ])

if test == True:
  print("Uploading Results")
  client.publish(topic="speedtest/ping", payload=str(results_dict["ping"]), qos=1, retain=False)
  client.publish(topic="speedtest/download", payload=str(results_dict["download"]/1000000), qos=1, retain=False)
  client.publish(topic="speedtest/upload", payload=str(results_dict["upload"]/1000000), qos=1, retain=False)
  print("Results Uploaded")
