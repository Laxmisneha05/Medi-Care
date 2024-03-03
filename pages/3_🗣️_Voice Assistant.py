import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import os

# Initialize speech recognizer
r = sr.Recognizer()

def voice_to_text():
    with sr.Microphone() as source:
        st.write("Speak something...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            st.write("You said:", text)
            return text
        except sr.UnknownValueError:
            st.write("Sorry, could not understand audio.")
        except sr.RequestError as e:
            st.write("Could not request results from Google Speech Recognition service; {0}".format(e))

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    # tts.save("output.mp3")
    # os.system("start output.mp3")

def main():
    st.title("Voice Assistant Streamlit App")
    st.write("Speak into your microphone to chat with the assistant!")

    text_to_speech("Voice Assistant is ready.")  # Call text_to_speech once before starting the loop

    while True:
        text = voice_to_text()
        if text:
            text_lower = text.lower()
            if "cardiac arrest" in text_lower:
                response = "I understand this can be frightening, but try to remain calm. Take deep breaths. I'm here with you."
            elif "seizure" in text_lower:
                response = "During a seizure, keep the person safe and comfortable. Do not restrain them. Time the seizure and call emergency services if it lasts longer than 5 minutes."
            elif "asthma attack" in text_lower:
                response = "If someone is having an asthma attack, help them sit upright, use their inhaler, and stay calm. If symptoms worsen, call emergency services."
            elif "diabetic emergency" in text_lower:
                response = "If someone is experiencing a diabetic emergency, offer them sugar or a sugary drink if they are conscious. If unconscious, do not give anything by mouth and call emergency services."
            elif "allergic reaction" in text_lower:
                response = "If someone is having a severe allergic reaction, administer an epinephrine auto-injector if available and call emergency services immediately."
            elif "burn" in text_lower:
                response = "For minor burns, cool the burn with cool running water for at least 10 minutes. For severe burns, call emergency services immediately."
            elif "heart attack" in text_lower:
                response = "If someone is having a heart attack, call emergency services immediately. Help them sit or lie down, and give them aspirin if available and they are able to swallow."
            elif "bleeding" in text_lower or "bleed" in text_lower:
                response = "Apply pressure to the wound with a clean cloth and elevate the injured area. If bleeding is severe, call emergency services."
            # Add more conditions and responses here for other medical emergencies
            else:
                response = "I'm sorry, I can only provide assistance for specific medical emergencies."
            st.write("Assistant:", response)
            text_to_speech(response)

if __name__ == "__main__":
    main()
