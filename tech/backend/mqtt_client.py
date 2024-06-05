import paho.mqtt.client as mqtt
from datetime import datetime
from database import get_db_connection

MQTT_BROKER = '192.168.50.179'
SENSOR_TOPIC = 'sensor/topic'
AUTOMATION_TOPIC = 'automation/topic'

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(SENSOR_TOPIC)
    client.subscribe(AUTOMATION_TOPIC)

def on_message(client, userdata, msg):
    conn = get_db_connection()
    if msg.topic == SENSOR_TOPIC:
        value = float(msg.payload.decode("utf-8").replace("\x00", ""))
        created_at = datetime.utcnow().isoformat()
        conn.execute('INSERT INTO sensor (created_at, value) VALUES (?, ?)', (created_at, value))
    elif msg.topic == AUTOMATION_TOPIC:
        state = msg.payload.decode()
        created_at = datetime.utcnow().isoformat()
        conn.execute('INSERT INTO automation (created_at, state) VALUES (?, ?)', (created_at, state))
    conn.commit()
    conn.close()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

def start_mqtt_client():
    client.connect(MQTT_BROKER, 1883, 60)
    client.loop_start()
