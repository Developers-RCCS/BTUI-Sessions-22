#include <Arduino.h>
#include <WiFi.h>
#include <FirebaseESP32.h>

//Provide the token generation process info.
#include "addons/TokenHelper.h"
//Provide the RTDB payload printing info and other helper functions.
#include "addons/RTDBHelper.h"

// Device ID
#define DEVICE_UID "1X"

// Your WiFi credentials
#define WIFI_SSID "wifi_id" // Enter your wifi ID
#define WIFI_PASSWORD "password" // Enter your wifi password

// Your Firebase Project Web API Key
#define API_KEY "API_key"
// Your Firebase Realtime database URL
#define DATABASE_URL "databse_url"

// Firebase Realtime Database Object
FirebaseData fbdo;
// Firebase Authentication Object
FirebaseAuth auth;
// Firebase configuration Object
FirebaseConfig config;
// Device Location config
String device_location = "Farm"; 
// Firebase database path
String databasePath = "";
// Firebase Unique Identifier
String fuid = ""; 
// Stores the elapsed time from device start up
unsigned long elapsedMillis = 0; 
// The frequency of sensor updates to firebase, set to 10seconds
unsigned long update_interval = 10000; 
// Dummy counter to test initial firebase updates
int count = 0; 
// Store device authentication status
bool isAuthenticated = false;

// Variables to hold sensor readings
float temperature = 0;
float humidity = 0;
float daytime = 0;
// JSON object to hold updated sensor values to be sent to be firebase
FirebaseJson temperature_json;
FirebaseJson humidity_json;
FirebaseJson daytime_json;
// connect ir sensor to arduino pin 2
int IRSensor = 2; 


void Wifi_Init() {
 WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
 Serial.print("Connecting to Wi-Fi");
 while (WiFi.status() != WL_CONNECTED){
  Serial.print(".");
  delay(300);
  }
 Serial.println();
 Serial.print("Connected with IP: ");
 Serial.println(WiFi.localIP());
 Serial.println();
}

void firebase_init() {
// configure firebase API Key
config.api_key = API_KEY;
// configure firebase realtime database url
config.database_url = DATABASE_URL;
// Enable WiFi reconnection 
Firebase.reconnectWiFi(true);
Serial.println("------------------------------------");
Serial.println("Sign up new user...");
// Sign in to firebase Anonymously
if (Firebase.signUp(&config, &auth, "", ""))
{
Serial.println("Success");
 isAuthenticated = true;
// Set the database path where updates will be loaded for this device
 databasePath = "/" + device_location;
 fuid = auth.token.uid.c_str();
}
else
{
 Serial.printf("Failed, %s\n", config.signer.signupError.message.c_str());
 isAuthenticated = false;
}
// Assign the callback function for the long running token generation task, see addons/TokenHelper.h
config.token_status_callback = tokenStatusCallback;
// Initialise the firebase library
Firebase.begin(&config, &auth);
}

void updateSensorReadings(){
Serial.println("------------------------------------");
Serial.println("Reading Sensor data ...");
temperature = 99;
humidity = 80;
float daytime = digitalRead (IRSensor);

// Check if any reads failed and exit early (to try again).
if (isnan(temperature) || isnan(humidity)) {
 Serial.println(F("Failed to read from DHT sensor!"));
 return;
 }
Serial.printf("Temperature reading: %.2f \n", temperature);
Serial.printf("Humidity reading: %.2f \n", humidity);
Serial.printf("Daytime reading: %.2f \n", daytime);
temperature_json.set("value", temperature);
humidity_json.set("value", humidity);
daytime_json.set("value", daytime);
}

void uploadSensorData() {
if (millis() - elapsedMillis > update_interval && isAuthenticated && Firebase.ready())
{
 elapsedMillis = millis();
 updateSensorReadings();
 String temperature_node = databasePath + "/temperature"; 
 String humidity_node = databasePath + "/humidity";
 String daytime_node = databasePath + "/daytime";

 if (Firebase.setJSON(fbdo, temperature_node.c_str(), temperature_json))
 {
 Serial.println("PASSED"); 
 Serial.println("PATH: " + fbdo.dataPath());
 Serial.println("TYPE: " + fbdo.dataType());
 Serial.println("ETag: " + fbdo.ETag());
 Serial.print("VALUE: ");
 printResult(fbdo); //see addons/RTDBHelper.h
 Serial.println("------------------------------------");
 Serial.println();
 }
 else
 {
 Serial.println("FAILED");
 Serial.println("REASON: " + fbdo.errorReason());
 Serial.println("------------------------------------");
 Serial.println();
 }
if (Firebase.setJSON(fbdo, humidity_node.c_str(), humidity_json))
{
 Serial.println("PASSED");
 Serial.println("PATH: " + fbdo.dataPath());
 Serial.println("TYPE: " + fbdo.dataType());
 Serial.println("ETag: " + fbdo.ETag()); 
 Serial.print("VALUE: ");
 printResult(fbdo); //see addons/RTDBHelper.h
 Serial.println("------------------------------------");
 Serial.println();
 }
 else
 {
 Serial.println("FAILED");
 Serial.println("REASON: " + fbdo.errorReason());
 Serial.println("------------------------------------");
 Serial.println();
  }
if (Firebase.setJSON(fbdo, daytime_node.c_str(), daytime_json))
 {
 Serial.println("PASSED"); 
 Serial.println("PATH: " + fbdo.dataPath());
 Serial.println("TYPE: " + fbdo.dataType());
 Serial.println("ETag: " + fbdo.ETag());
 Serial.print("VALUE: ");
 printResult(fbdo); //see addons/RTDBHelper.h
 Serial.println("------------------------------------");
 Serial.println();
 }
 else
 {
 Serial.println("FAILED");
 Serial.println("REASON: " + fbdo.errorReason());
 Serial.println("------------------------------------");
 Serial.println();
 }

 }
}

void setup() {
// Initialise serial communication for local diagnostics
Serial.begin(115200);
// Initialise Connection with location WiFi
Wifi_Init();
// Initialise firebase configuration and signup anonymously
firebase_init();
// Initialise IR Sensor
pinMode (IRSensor, INPUT); // sensor pin INPUT

// Initialise temperature and humidity json data
temperature_json.add("deviceuid", DEVICE_UID);
temperature_json.add("name", "DHT11-Temp");
temperature_json.add("type", "Temperature");
temperature_json.add("location", device_location);
temperature_json.add("value", temperature);
// Print out initial temperature values
String jsonStr;
temperature_json.toString(jsonStr, true);
Serial.println(jsonStr);

humidity_json.add("deviceuid", DEVICE_UID);
humidity_json.add("name", "DHT11-Hum");
humidity_json.add("type", "Humidity");
humidity_json.add("location", device_location);
humidity_json.add("value", humidity);
// Print out initial humidity values
String jsonStr2;
humidity_json.toString(jsonStr2, true);
Serial.println(jsonStr2);

daytime_json.add("deviceuid", DEVICE_UID);
daytime_json.add("name", "DHT11-Hum");
daytime_json.add("type", "Humidity");
daytime_json.add("location", device_location);
daytime_json.add("value", daytime);
// Print out initial humidity values
String jsonStr3;
daytime_json.toString(jsonStr3, true);
Serial.println(jsonStr3);
}

void loop() {
 uploadSensorData();
 }
