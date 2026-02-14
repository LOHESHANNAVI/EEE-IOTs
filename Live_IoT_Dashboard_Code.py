import streamlit as st
import paho.mqtt.client as mqtt
import threading

st.set_page_config(page_title="Live Buck Monitor", layout="wide")

st.title("⚡ Live Buck Converter Monitor")

# Shared data
data = {"voltage": 240, "current": 5}

# MQTT callback
def on_message(client, userdata, message):
    payload = message.payload.decode()
    voltage, current = payload.split(",")
    data["voltage"] = float(voltage)
    data["current"] = float(current)

# MQTT setup
def mqtt_thread():
    client = mqtt.Client()
    client.on_message = on_message
    client.connect("broker.hivemq.com", 1883)
    client.subscribe("buck/data")
    client.loop_forever()

threading.Thread(target=mqtt_thread, daemon=True).start()

# UI Auto Refresh
st_autorefresh = st.empty()

voltage = data["voltage"]
current = data["current"]
power = voltage * current

col1, col2, col3 = st.columns(3)

col1.metric("Voltage (V)", f"{voltage:.2f}")
col2.metric("Current (A)", f"{current:.2f}")
col3.metric("Power (W)", f"{power:.2f}")