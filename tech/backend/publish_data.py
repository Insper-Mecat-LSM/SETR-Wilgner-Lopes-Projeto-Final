import paho.mqtt.client as mqtt
import time
import random

MQTT_BROKER = '192.168.50.179'
SENSOR_TOPIC = 'sensor/topic'
AUTOMATION_TOPIC = 'automation/topic'

def publish_sensor_data(client):
    value = random.uniform(10.0, 40.0)  # Simula um valor de sensor entre 20.0 e 30.0
    client.publish(SENSOR_TOPIC, str(value))
    print(f"Published to {SENSOR_TOPIC}: {value}")

def publish_automation_data(client):
    state = random.choice(['a', 'b', 'c'])  # Simula um estado 'a', 'b' ou 'c'
    client.publish(AUTOMATION_TOPIC, state)
    print(f"Published to {AUTOMATION_TOPIC}: {state}")

def main():
    client = mqtt.Client()
    client.connect(MQTT_BROKER, 1883, 60)
    client.loop_start()

    try:
        while True:
            publish_sensor_data(client)
            time.sleep(1)  # Publica a cada 5 segundos

            publish_automation_data(client)
            time.sleep(1)  # Publica a cada 5 segundos

    except KeyboardInterrupt:
        print("Stopped by user")
    finally:
        client.loop_stop()
        client.disconnect()

if __name__ == "__main__":
        main()
