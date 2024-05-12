import streamlit as st

st.set_page_config(page_title="MediConnect")

st.header("Transcribed Audio")
with open('Transcribe.txt', 'r') as file:
    default_text = file.read()

with st.container():  
    text_input = st.text_area("Transcription", value=default_text, key="transcription_input",height=150)
    st.session_state["default_text"] = text_input

submit = st.button("Generate SOAP Notes")

transcription=""

def change_trans():
    transcription = st.session_state["default_text"]
    with open("Transcribe.txt", "w") as file:
        file.write(transcription)

if submit:
    change_trans()
    st.switch_page("pages/SOAP.py")
                

submit2 = st.button("Generate Prescription")

if submit2:
    change_trans()
    st.switch_page("pages/Prescription.py")














