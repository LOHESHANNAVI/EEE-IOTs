#  bulk converter

import streamlit as st
import matplotlib.pyplot as plt

st.title("Buck Converter Monitor")

voltage = str(input('GIVE ME THE VOLTAGE'))
current = str(input('GIVE ME THE CURRENT'))

power = voltage * current

st.metric("Output Voltage", voltage)
st.metric("Output Current", current)

st.metric("Output Power", power)
