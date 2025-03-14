# MQTT-Based Light Control System

A simple web-based application that allows controlling a virtual light via MQTT. The system consists of two main components:

1. **Web Interface**: A browser-based UI with buttons to turn the light on and off.
2. **IoT Device Simulator**: A Python script that simulates an ESP8266 device, which connects to the MQTT broker to receive commands.

This project is designed to demonstrate the power of MQTT in IoT systems for controlling devices remotely.

---

## Components

### Web Interface (index.html)

A simple HTML page with JavaScript that:

- Connects to a public MQTT broker via WebSockets
- Provides **"Turn ON"** and **"Turn OFF"** buttons to control the virtual light
- Displays the current light status (ON or OFF)
- Publishes messages to the MQTT topic `/student_group/light_control` when you press the buttons

### IoT Device Simulator (light_simulation.py)

A Python script that:

- Connects to the same MQTT broker
- Subscribes to the `/student_group/light_control` topic to receive commands
- Prints the light status to the terminal whenever a message is received from the web interface (turning the light on or off)

---

## How to Run the Project Locally

To run this project on your local machine, follow the steps below:

### Step 1: Clone the Repository

Clone the repository to your local machine using Git:

````bash
git clone https://github.com/Paulin-NIYOBYOSE/mqtt-light-control.git
cd mqtt-light-control

### Step 2: Insall dependencies

```bash
pip install paho-mqtt

### Step 3: Run the project
```bash
python light_simulation.py

### Run also the index.html file




````
