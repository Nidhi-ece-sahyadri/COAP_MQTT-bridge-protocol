# COAP_MQTT-bridge-protocol
This project integrates CoAP and MQTT for efficient IoT communication. An ESP32 acts as a CoAP server sending sensor data to a PC client, which bridges and publishes it to the Mosquitto MQTT broker. Node-RED subscribes to the topics and visualizes temperature and humidity on a live dashboard.
# ✅ IoT Sensor Monitoring using CoAP and MQTT


## 📌 Overview  
This project demonstrates a **hybrid IoT architecture** combining **CoAP** (for local, lightweight communication) and **MQTT** (for cloud-based remote monitoring).  
An **ESP32** device acts as a CoAP server, sending **temperature** and **humidity** data to a **PC-based bridge**, which then forwards the data to the **Mosquitto MQTT Broker**.  
The **Node-RED dashboard** subscribes to MQTT topics to visualize the live sensor data remotely.

---

## 📐 System Architecture  

<img width="765" height="544" alt="Screenshot 2025-08-04 195747" src="https://github.com/user-attachments/assets/de134542-671d-43c4-b712-599551be35a2" />




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
ESP32 runs a CoAP server exposing a single endpoint:
- `coap://<ESP32-IP>/sensor`

It responds to GET requests with a combined message:
`Temperature: 28.5C, Humidity: 70.2%`


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
  
 📥 How to Import into Node-RED
 
Open Node-RED in your browser:
`http://localhost:1880`

Click on the menu (☰) → Import

Paste the JSON above

Click Import

Click Deploy

Go to the dashboard:
`http://localhost:1880/ui`


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

`GET handler for /sensor`

The ESP32 CoAP server exposes a single resource `/sensor`, which returns both temperature and humidity in a single response like:

`"Temperature: 28.5C, Humidity: 70.2%"`

## 🧰 Install Node-RED
---

    npm install -g --unsafe-perm node-red








## 💻 Python CoAP Client + MQTT Publisher
Install dependencies:

## 🧰 Install Node-RED
---

    npm install -g --unsafe-perm node-red

Fetches sensor data via CoAP and Publishes data to MQTT

    ```
     pip install aiocoap paho-mqtt
Run the bridge script:

    ```

        python bridge.py


Replace <ESP32-IP> with the actual local IP of your ESP32 in the script.

## 🌐 Node-RED Dashboard
Subscribe to the topics:
      ```
                
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





