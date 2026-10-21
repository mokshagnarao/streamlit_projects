import streamlit as st
import requests

st.title("Weather API Demo")

API_KEY = st.secrets.get("demo_key")

city = st.text_input("Enter city", "Chennai")

if st.button("Get Weather"):

    #OpenWeather API URL
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    resp = requests.get(url).json()

    #Display full API response
    st.json(resp)

    #Extract required values
    if "main" in resp:
        temperature = resp["main"]["temp"]
        humidity = resp["main"]["humidity"]
        condition = resp["weather"][0]["main"]

        c1, c2, c3 = st.columns(3)

        c1.metric("Temperature", f"{temperature}°C")
        c2.metric("Condition", condition)
        c3.metric("Humidity", f"{humidity}%")

    else:
        st.error("City not found or API key is invalid.")

    st.markdown("---")

    st.subheader("HTTP Methods")

    st.markdown("""- **GET** → Retrieve data- **POST** → Send data- **PUT** → Update data- **DELETE** → Delete data""")