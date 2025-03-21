import streamlit as st
import requests

st.title("ML Prediction App")

num = st.number_input("Enter a number:")

if st.button("Predict"):
    response = requests.post(
        #"https://your-fastapi-url.onrender.com/predict",  # TEMP placeholder
        "http://localhost:8000/predict",
        json={"number": num}
    )
    result = response.json()
    st.write("Prediction:", result["prediction"])
