import paho.mqtt.client as mqtt
import time
import sys

# MQTT Configuration
BROKER_ADDRESS = "broker.emqx.io"
PORT = 1883
TOPIC = "/student_group/light_control"
CLIENT_ID = "python_iot_simulator"


# Callback when connected to MQTT broker
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("✅ Connected to MQTT Broker!")
        # Subscribe to the topic
        client.subscribe(TOPIC)
        print(f"📡 Listening for messages on {TOPIC}")
    else:
        print(f"❌ Failed to connect, return code {rc}")
        sys.exit(1)


# Callback when message is received
def on_message(client, userdata, msg):
    message = msg.payload.decode()
    print(f"📩 Message received: {message}")

    if message == "ON":
        print("💡 Light is TURNED ON")
    elif message == "OFF":
        print("💡 Light is TURNED OFF")
    else:
        print(f"⚠️ Unknown command: {message}")


# Set up MQTT client with specified protocol version and callback API version
client = mqtt.Client(client_id=CLIENT_ID, callback_api_version=mqtt.CallbackAPIVersion.VERSION1)
client.on_connect = on_connect
client.on_message = on_message

# Connect to broker
print(f"🔄 Connecting to MQTT broker at {BROKER_ADDRESS}...")
try:
    client.connect(BROKER_ADDRESS, PORT, 60)
except Exception as e:
    print(f"❌ Connection failed: {e}")
    sys.exit(1)

# Start the loop
try:
    print("🚀 ESP8266 simulator started. Press Ctrl+C to exit.")
    client.loop_forever()
except KeyboardInterrupt:
    print("\n🛑 Simulator stopped by user")
    client.disconnect()
    sys.exit(0)