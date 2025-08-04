# COAP_MQTT-bridge-protocol
This project integrates CoAP and MQTT for efficient IoT communication. An ESP32 acts as a CoAP server sending sensor data to a PC client, which bridges and publishes it to the Mosquitto MQTT broker. Node-RED subscribes to the topics and visualizes temperature and humidity on a live dashboard.
# ✅ IoT Sensor Monitoring using CoAP and MQTT

## 📌 Overview  
This project demonstrates a **hybrid IoT architecture** combining **CoAP** (for local, lightweight communication) and **MQTT** (for cloud-based remote monitoring).  
An **ESP32** device acts as a CoAP server, sending **temperature** and **humidity** data to a **PC-based bridge**, which then forwards the data to the **Mosquitto MQTT Broker**.  
The **Node-RED dashboard** subscribes to MQTT topics to visualize the live sensor data remotely.

---

## 📐 System Architecture  

    ![Uploading image.png…]()



---

## 🧠 Key Components & Their Roles

| Component                    | Role                         | Purpose                                                      |
|-----------------------------|------------------------------|--------------------------------------------------------------|
| **ESP32**                   | CoAP Server                  | Hosts temperature & humidity data, responds to CoAP requests |
| **Your PC**                 | CoAP Client + MQTT Publisher | Requests sensor data, publishes it to MQTT topics            |
| **Mosquitto (Public Broker)** | MQTT Broker                  | Relays MQTT messages to cloud clients                        |
| **Node-RED**                | MQTT Subscriber               | Subscribes to topics and displays sensor data                |
| **Mobile CoAP Client (Optional)** | CoAP Client (Local only)      | Directly queries ESP32 within local network only             |

---

## 🔁 Step-by-Step Data Flow

### 🔹 1. ESP32 CoAP Server  
ESP32 runs a CoAP server exposing:
- `coap://<ESP32-IP>/temperature`
- `coap://<ESP32-IP>/humidity`

It responds to GET requests with current sensor readings.

### 🔹 2. PC Bridge (CoAP Client + MQTT Publisher)  
The Python client running on your PC:
- Sends GET requests to ESP32 using `aiocoap`
- Publishes the received data to:
  - `mytest/temp`
  - `mytest/humi`  
using the **Mosquitto public broker** (`mqtt://test.mosquitto.org`)

### 🔹 3. Node-RED Dashboard  
Node-RED subscribes to the MQTT topics using MQTT IN nodes.  
It visualizes:
- Text values (`ui_text`)
- Gauges (`ui_gauge`) for temperature and humidity

---

## ⚡ Advantages of CoAP + MQTT Hybrid

✅ **CoAP** is ideal for **local lightweight communication** (UDP, low power, simple implementation)

✅ **MQTT** enables **remote monitoring**, even when not on the same Wi-Fi network

✅ By bridging **CoAP to MQTT**, the system:
- Collects real-time data locally (low overhead)
- Sends it to the cloud (internet) for remote access
- Removes the limitation of CoAP's local-only reach

---

## 💻 Technologies Used

- **ESP32** (Arduino with CoAP Simple library)
- **Python** (with `aiocoap` and `paho-mqtt`)
- **Mosquitto** Public MQTT Broker
- **Node-RED** Dashboard UI

---

## 🔧 Setup & Commands

### 🧠 ESP32 (CoAP Server)
Flash the ESP32 with code that creates a CoAP server:
     ```cpp
             
              
              GET handlers for /temperature and /humidity






## 💻 Python CoAP Client + MQTT Publisher
Install dependencies:


    ```cpp
     pip install aiocoap paho-mqtt
Run the bridge script:

           ```cpp

            python bridge.py


Replace <ESP32-IP> with the actual local IP of your ESP32 in the script.

## 🌐 Node-RED Dashboard
Subscribe to the topics:
      ```cpp
                
                mytest/temp

            mytest/humi

- Use:

ui_text node to show text values

ui_gauge node to visualize data



## 📊  Dashboard View
-🌡️ Temperature shown via gauge and text

-💧 Humidity visualized in real-time

-Accessible from any device with internet

## 📝 Summary
-This project demonstrates how to:

-Collect sensor data using CoAP

-Bridge that to MQTT

-Monitor remotely using Node-RED

-It is a scalable and efficient architecture for IoT environments where local sensing and remote access are both critical.





