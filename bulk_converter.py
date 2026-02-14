#  bulk converter

import streamlit as st
import matplotlib.pyplot as plt

st.title("Buck Converter Monitor")

voltage = 12  # example
current = 2

power = voltage * current

st.metric("Output Voltage", voltage)
st.metric("Output Current", current)
st.metric("Output Power", power)