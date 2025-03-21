import streamlit as st
import requests

st.title("ML Prediction App")

num = st.number_input("Enter a number:")

if st.button("Predict"):
    try:
        response = requests.post(
            "https://view-s3-file.onrender.com/predict",  # Replace with your real URL
            json={"number": num}
        )

        st.write("Status code:", response.status_code)
        st.write("Raw response:", response.text)

        result = response.json()
        st.write("Prediction:", result["prediction"])
    except Exception as e:
        st.error(f"Failed to get prediction: {e}")
