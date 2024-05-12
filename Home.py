import assemblyai as aai
import streamlit as st

st.set_page_config(page_title="MediConnect")

aai.settings.api_key = st.secrets["assembly"]["assembly_api_key"]
st.header("Choose audio file")
uploaded_file = st.file_uploader(" ")
transcriber = aai.Transcriber()

if uploaded_file is not None:
    st.write("File uploaded successfully.")
    Transcribe_Button = st.button("Transcribe Audio")

    if Transcribe_Button:
        transcript = transcriber.transcribe(uploaded_file)

        if transcript.status == aai.TranscriptStatus.error:
            print(transcript.error)
        else:
            with open("Transcribe.txt", "w") as file:
                file.write(transcript.text)
            st.switch_page("pages/Transcribe.py")

