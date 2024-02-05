import os
import streamlit as st
from agent import TranslationAgent


agent = TranslationAgent(src='en', dest='ur')
languages = agent.get_lang()
path = 'audio/translated.mp3'

st.title("Speech Translation Agent")
st.sidebar.header("Choose Language")

agent.src = st.sidebar.selectbox(
    "Source Language",
    list(languages.keys()), format_func=lambda x: languages[x]
)
agent.dest = st.sidebar.selectbox(
    "Destination Language",
    list(languages.keys()), format_func=lambda x: languages[x]
)

st.text("Record speech, get translation, and enjoy audio playback.")

if st.button("Speak Now"):

    spoken_text = agent.speak_now()

    if spoken_text:
        st.text("Recording Complete!")

        try:
            os.remove(path)
        except Exception as e:
            print(f"An error occurred: {e}")

        with st.expander("Original Text"):
            st.text(spoken_text)

        translated_text = agent.translate(spoken_text)

        with st.expander("Translated Text", expanded=True):
            st.text(translated_text)
            agent.save_audio(translated_text, path=path)
            agent.play_audio(path=path)

    else:
        st.text('Speak Again!!!')
