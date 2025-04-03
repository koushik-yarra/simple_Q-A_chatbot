from dotenv import load_dotenv

# load all the environment variables from the .env file  

load_dotenv()

# import requires libraries
import streamlit as st
import os
import google.generativeai as genai # type: ignore # import generativeai module

# configure api key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load gemini model to get response

model = genai.GenerativeModel("gemini-2.0-flash")
def get_gemini_response(prompt):
    response=model.generate_content(prompt)
    return response.text


# streamlit app

st.set_page_config(page_title="Q&A AI")
st.title(" SIMPLE CHATBOT")
input_text = st.text_input("Enter your question here",key="input_text")
submit_button = st.button("Submit")

if submit_button:
    response=get_gemini_response(input_text)
    st.write(response)