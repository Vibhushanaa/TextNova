import requests
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "Bearer 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"}

def query(uploaded_file):
    # Read the content of the uploaded file directly
    data = uploaded_file.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

uploaded_file = st.file_uploader("Upload an image", type="jpg")

if uploaded_file is not None:
    if st.button("Click"):
        output = query(uploaded_file)
        st.write(output)

