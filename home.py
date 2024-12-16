import streamlit as st
import requests
import time

RASPBERRY_PI_URL = "https://water-monitoring-system.ngrok.io/data"  # Replace with the actual IP

def read_data():
    try:
        response = requests.get(RASPBERRY_PI_URL, timeout=1)
        return response.json()
    except requests.exceptions.RequestException:
        return {"flow_rate": 0, "total_water_flow": 0}

st.title("Water Flow Monitoring System")

flow_rate_placeholder = st.empty()
total_flow_placeholder = st.empty()

while True:
    data = read_data()
    flow_rate_placeholder.metric(label="Flow Rate (L/min)", value=f"{data['flow_rate']:.2f}")
    total_flow_placeholder.metric(label="Total Water Flow Today (L)", value=f"{data['total_water_flow']:.2f}")
    time.sleep(1)
