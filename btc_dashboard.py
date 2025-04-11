import streamlit as st
import requests
import pandas as pd
from datetime import datetime
import time

st.set_page_config(page_title="Live BTC and SOL Tracker", layout="wide")
st.title("💰 Live BTC and SOL Tracker")
st.caption("Powered by CoinGecko API, updates every 30 seconds")

# Initialize price histories
if "btc_history" not in st.session_state:
    st.session_state.btc_history = pd.DataFrame(columns=["Time", "Price"])

if "sol_history" not in st.session_state:
    st.session_state.sol_history = pd.DataFrame(columns=["Time", "Price"])

# Corrected API URL
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,solana&vs_currencies=usd,gbp"
response = requests.get(url).json()

now = datetime.now().strftime("%H:%M:%S")

if "bitcoin" in response and "solana" in response:
    btc_price = response["bitcoin"]["usd"]
    sol_price = response["solana"]["usd"]

    # Append new data points
    st.session_state.btc_history.loc[len(st.session_state.btc_history)] = [now, btc_price]
    st.session_state.sol_history.loc[len(st.session_state.sol_history)] = [now, sol_price]
else:
    st.warning("❌ Could not fetch BTC or SOL data.")

# Layout with two columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("🟠 Bitcoin (BTC)")
    st.metric("Price (USD)", f"${btc_price:,.2f}")
    st.line_chart(st.session_state.btc_history.set_index("Time"))

with col2:
    st.subheader("🟣 Solana (SOL)")
    st.metric("Price (USD)", f"${sol_price:,.2f}")
    st.line_chart(st.session_state.sol_history.set_index("Time"))

# Refresh every 30 seconds
time.sleep(30)
st.rerun()

