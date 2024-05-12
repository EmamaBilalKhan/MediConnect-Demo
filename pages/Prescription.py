import streamlit as st

import google.generativeai as genai

genai.configure(api_key=st.secrets["gemini"]["gemini_api_key"])

model = genai.GenerativeModel('gemini-pro')

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title="MediConnect")

st.header("Prescription")

with open('Transcribe.txt', 'r') as file:
    default_text = file.read()

response=get_gemini_response("Generate prescription from the following Patient Doctor Conversation, the pattern to follow for prescription is the standard prescription pattern of international doctors:"+default_text)
st.write(response)
    
        






