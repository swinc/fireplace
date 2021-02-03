#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>

ESP8266WiFiMulti WiFiMulti;

/*
 * check once an hour to the Pi
 * if pi says green, turn light to green
 * if pi says red, turn light to red
 * if pi says something we can't recognize, blink red
 * if can't connect to wifi, blink both
 */

/* === GLOBALS === */
char* ssid = "";
char* wifiPassword = "";

const int greenPin = 5;
const int redPin = 0;

void setup() {
  Serial.begin(9600);
  delay(1000); // allow Serial setup before printing
  Serial.println('Begin serial output...');

  Serial.println('Setting pin modes...');
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  Serial.print('done');
}

void connectToWifi() {
  WiFi.mode(WIFI_STA);
  WiFiMulti.addAP(ssid, wifiPassword);

  Serial.print("Connecting to wifi...");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
    // TODO: blink both lights while connecting
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
}

String getColorFromPi() {
  WiFiClient client;
  HTTPClient http;

  char* host = "http://192.168.4.78/light.html";
  String color = "";

  Serial.printf("\nGETTING %s...\n", host);
  if (!http.begin(client, host)) { // if cannot connect
    Serial.println("[HTTP] Unable to connect to website");
  }

  int httpCode = http.GET();
  if (httpCode < 0) { // http response will be negative on error
    Serial.printf("HTTP error: %s\n", http.errorToString(httpCode).c_str());
  }

  Serial.printf("GET code is: %d\n", httpCode);
  if (httpCode == HTTP_CODE_OK) {
    color = http.getString();
    Serial.printf("Server response: %s\n", color.c_str());
  } else {
    Serial.printf("Error: %s\n", http.errorToString(httpCode).c_str());
  }

  http.end();

  return color;
}

void loop() {
  connectToWifi();
  String color = getColorFromPi();

  if(color == "green") {
    Serial.println("Server responds with 'green'; setting light to green.");
    digitalWrite(greenPin, HIGH);
    digitalWrite(redPin, LOW);
  } else if(color == "red") {
    Serial.println("Server did not respond with 'green'; setting light to red.");
    digitalWrite(greenPin, LOW);
    digitalWrite(redPin, HIGH);
  } else {
    // TODO: blinkRed();
  }

  Serial.println("Sleeping for 60 minutes. Good night!");
  delay(60 * 60 * 1000); // wait 60 minutes
}
