# Buck Converter Monitor

import streamlit as st
import matplotlib.pyplot as plt

st.title("Buck Converter Monitor")

# Use Streamlit input fields
voltage = st.number_input("Enter Voltage (V)", min_value=0.0)
current = st.number_input("Enter Current (A)", min_value=0.0)

power = voltage * current

st.metric("Output Voltage (V)", voltage)
st.metric("Output Current (A)", current)
st.metric("Output Power (W)", power)
