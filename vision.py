from dotenv import load_dotenv
load_dotenv()  # Load all environment variables

import streamlit as st
from PIL import Image
import os
import google.generativeai as genai


# Configure the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load gemini model and generate text
model = genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(question, image):
    if question:
        response = model.generate_content([question, image])
    else:
        response = model.generate_content([image])
    return response.text

# Initializing the page
st.set_page_config(
    page_title="PicScribe AI",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Add background gradient using CSS
st.markdown(
    """
    <style>
    .reportview-container {
        background: linear-gradient(to right, #0575E6, #021B79);
        color: white;
    }
    .sidebar .sidebar-content {
        background: linear-gradient(to right, #0575E6, #021B79);
        color: white;
    }
    .stTextInput label {
        color: white;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Creating beautiful UI using Streamlit
st.header("PicScribe AI")
st.write("Ask any question and get a response ")

question = st.text_input("Enter your question", key="input")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

submit = st.button("Tell me about the image")

# When the submit button is clicked
if submit and image is not None:
    response = get_gemini_response(question, image)
    st.subheader("Response")
    st.write(response)
