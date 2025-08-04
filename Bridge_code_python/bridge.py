import asyncio
import time
import os
from aiocoap import *
import paho.mqtt.client as mqtt

# ========== CONFIG ========== #
ESP32_IP = "192.168.216.218"         # Replace with your ESP32 IP
RESOURCE = "sensor"                  # CoAP resource endpoint
MQTT_BROKER = "test.mosquitto.org"  # ✅ Use mosquito public broker
MQTT_PORT = 1883                   # ✅ Default MQTT port

MQTT_TOPIC_TEMP = "mytest/temp"
MQTT_TOPIC_HUMI = "mytest/humi"
MQTT_USERNAME = ""                   # Optional: add if needed
MQTT_PASSWORD = ""                   # Optional: add if needed

# ========== FETCH FROM ESP32 ========== #
async def get_coap_data():
    print("📤 Sending CoAP GET request...")
    protocol = await Context.create_client_context()
    await asyncio.sleep(1)

    request = Message(code=GET, uri=f'coap://{ESP32_IP}/{RESOURCE}', mtype=NON)

    try:
        response = await protocol.request(request).response
        print("✅ CoAP response received")
        payload = response.payload.decode('utf-8')
        print(f"📨 Payload: {payload}")
        return payload
    except Exception as e:
        print(f"❌ Failed to fetch CoAP data: {e}")
        return None

# ========== PUBLISH TO MQTT ========== #
def publish_to_mqtt(raw_message):
    client = mqtt.Client()

    # 🔐 Optional MQTT Auth (skip if using public broker)
    if MQTT_USERNAME and MQTT_PASSWORD:
        client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

    try:
        # Parse "Temperature: 30.2C, Humidity: 85.0%"
        temp = raw_message.split(",")[0].split(":")[1].strip().replace("C", "")
        hum = raw_message.split(",")[1].split(":")[1].strip().replace("%", "")

        client.connect(MQTT_BROKER, MQTT_PORT, 60)
        client.loop_start()

        client.publish(MQTT_TOPIC_TEMP, temp, retain=True)
        client.publish(MQTT_TOPIC_HUMI, hum, retain=True)

        time.sleep(1)  # Ensure messages are sent
        client.loop_stop()
        client.disconnect()

        print(f"📡 Published temp → {MQTT_TOPIC_TEMP}: {temp}")
        print(f"📡 Published humi → {MQTT_TOPIC_HUMI}: {hum}")

    except Exception as e:
        print(f"❌ MQTT publish failed or parse error: {e}")

# ========== LOOP ========== #
async def main():
    while True:
        data = await get_coap_data()
        if data:
            publish_to_mqtt(data)
        await asyncio.sleep(5)

# ========== RUN ========== #
if __name__ == "__main__":
    asyncio.run(main())
