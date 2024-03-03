import streamlit as st

def main():
    st.title("FAQ - MedAI Emergency Response System")

    st.header("1. How does the system assess the urgency of a healthcare emergency?")
    st.write("The system utilizes advanced algorithms for voice analysis, including speech rate, tone, and anxiety level, to assess the urgency and severity of the healthcare emergency. Additionally, it extracts relevant information from the caller's spoken words to understand the specific medical issue being faced.")

    st.header("2. Can the system handle video calls?")
    st.write("Yes, the system integrates computer vision techniques to enable video calls for situations where visual information is essential for accurate diagnosis and intervention. Facial expression analysis and object recognition are used to assess the caller's condition, identify medical symptoms, and provide additional context for the emergency response.")

    st.header("3. How does the AI-driven emergency response work?")
    st.write("The system implements an AI-powered decision-making module that interprets the collected data to determine the appropriate course of action for the healthcare emergency. This includes identifying potential medical emergencies, such as cardiac arrest, strokes, or severe injuries, and generating personalized response plans based on the severity and urgency of the situation.")

    st.header("4. Is the AI's decision-making process transparent?")
    st.write("Yes, the system incorporates explainable AI (XAI) techniques to provide transparent reasoning behind its decisions and recommendations. It generates human-understandable explanations for the actions taken, ensuring that healthcare professionals and patients can comprehend the rationale behind the provided guidance and assistance.")

    st.header("5. What kind of guidance and assistance does the system provide?")
    st.write("The system provides real-time guidance and assistance to the caller, including first aid instructions, steps to stabilize the patient's condition, and recommendations for seeking further medical assistance from nearby healthcare facilities or emergency services. It prioritizes providing clear, concise, and actionable advice to the caller and any bystanders present.")

if __name__ == "__main__":
    main()