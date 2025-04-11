import streamlit as st
import requests
import time

st.set_page_config(page_title="Live BTC Tracker", layout="wide")

st.title("💰 Live Bitcoin Price Tracker")
st.caption("Powered by CoinGecko API, updates every 20 seconds")

placeholder = st.empty()

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd,gbp"

while True:
    response = requests.get(url).json()

    if "bitcoin" in response:
        usd = response["bitcoin"]["usd"]
        gbp = response["bitcoin"]["gbp"]

        with placeholder.container():
            st.metric("Bitcoin Price (USD)", f"${usd:,.2f}")
            st.metric("Bitcoin Price (GBP)", f"£{gbp:,.2f}")
    else:
        st.warning("Could not fetch Bitcoin data.")

    time.sleep(20)