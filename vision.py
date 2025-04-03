### CHAT WITH IMAGES
# 
# 
from dotenv import load_dotenv
# load all the environment variables from the .env file  
load_dotenv()
# import requires libraries
import streamlit as st
import os
import google.generativeai as genai # type: ignore # import generativeai module
from PIL import Image
# configure api key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# function to load gemini model to get response
model = genai.GenerativeModel("gemini-2.0-flash-lite")
def get_gemini_response(prompt,image):
    if input!="":
        response=model.generate_content([prompt,image])
    else:
        response=model.generate_content(image)
    return response.text

# streamlit app

st.set_page_config(page_title="Q&A IMAGE AI")
st.title("Basic Q&A  Image and Text Chatbot")
input_text = st.text_input("Enter your question here",key="input_text")
upload = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
image=""
if upload is not None:
    image = Image.open(upload)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

submit_button = st.button("Ask the question")
response=get_gemini_response(input_text,image)
if submit_button:
    st.write(response)