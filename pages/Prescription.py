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

response=get_gemini_response("Generate prescription from the following Patient Doctor Conversation, the pattern to follow should be standard pattern for prescription, it should include:Patient Name, Doctor Name, Date, Prescribed Medicine and dosage, strength, quantity refills and how to take and when to take for each medicine prescribed, doctor's signature, any recommended tests/treatments etc:"+default_text)
st.write(response)
    
        






