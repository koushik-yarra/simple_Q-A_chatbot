# simple Q&A chatbot with chat history
from dotenv import load_dotenv
load_dotenv() # loading all the environment variables from the .env file

# import required libraries

import streamlit as st
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#function to load gemini model to get response

model=genai.GenerativeModel("gemini-2.0-flash")

chat=model.start_chat(history=[])

def get_gemini_response(prompt):
    response=chat.send_message(prompt,stream=True)
    return response

# streamlit app

st.set_page_config(page_title="Q&A AI")
st.title("AI CHATBOT")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]

input_text = st.text_input("Enter your question here",key="input_text")
submit_button = st.button("Submit")

if submit_button and input_text:
    response=get_gemini_response(input_text)
    # add user query and response to chat history
    st.session_state['chat_history'].append(("you",input_text))
    st.subheader("Response:")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("bot",chunk.text))

st.subheader("Chat History:")
for speaker, text in st.session_state['chat_history']:
    if speaker=="you":
        st.write("You: "+text)
    else:
        st.write("Bot: "+text)