#include <WiFi.h>
#include <coap-simple.h>
#include <DHT.h>

const char* ssid = "nidhiyashu";
const char* password = "12345678";

// DHT11 configuration
#define DHTPIN 4        // GPIO pin connected to DHT11
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

// CoAP
WiFiUDP udp;
Coap coap(udp);

// Callback function for incoming CoAP requests
void callback(CoapPacket &packet, IPAddress ip, int port) {
  Serial.println("📩 Received CoAP Request");

  float temperature = dht.readTemperature(); // Read temperature in Celsius
  float humidity = dht.readHumidity();       // Read humidity

  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("❌ Failed to read from DHT sensor!");
    coap.sendResponse(ip, port, packet.messageid, "Error reading sensor");
    return;
  }

  // Prepare response message
  String responseStr = "Temperature: " + String(temperature, 1) + "C, Humidity: " + String(humidity, 1) + "%";
  Serial.println("📤 Sending Response: " + responseStr);

  // ✅ Send response including token (fix for aiocoap client compatibility)
 coap.sendResponse(
  ip,
  port,
  packet.messageid,
  responseStr.c_str(),
  responseStr.length(),
  COAP_CONTENT,
  COAP_TEXT_PLAIN,  // ✅ Correct
  packet.token,
  packet.tokenlen
);


}

void setup() {
  Serial.begin(115200);
  Serial.println("🚀 Starting ESP32 CoAP Server...");

  dht.begin(); // Start DHT sensor

  WiFi.begin(ssid, password);
  Serial.print("🔌 Connecting to WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\n✅ Connected to WiFi");
  Serial.print("📡 ESP32 IP Address: ");
  Serial.println(WiFi.localIP());

  // Set up CoAP server
  coap.server(callback, "sensor");
  coap.start();
  Serial.println("📡 CoAP Server started. Listening at /sensor");
}

void loop() {
  coap.loop(); // Handle CoAP requests
}
