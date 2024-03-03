import streamlit as st
from pathlib import Path
import google.generativeai as genai

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the API key from the environment variables
api_key = os.getenv("API_KEY")

genai.configure(api_key="AIzaSyCvvnQqjhuK4COdR9s1_E1Te69nTqtp-o0")

generation_config = {
    "temperature": 0.4,
    "top_p": 1,
    "top_k" : 32,
    "max_output_tokens": 4096,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]


system_prompt="""
As a highly skilled medical practitioner specializing in image analysis, you are tasked with examing medical images for reowned hospital. Your expertise is crucial in identifying anamalies, diseases, or health issues that may be present in the images.

Your Responsibilities include:

1. Detailed Analysis: Throughly analyze each image, focusing on identifying any abnormal findings.
2. Findings Report: Document all observed anomalies or signs of disease. Clearly articulate these findings in a structured format.
3. Recommendations and Next steps: Based on your analysis, suggest potential next steps, including further tests or treatments as applicable.
4. Treatment Suggestions: If appropriate, recommend possible treatment options or interventions 
Important Notes:

1. Scope of Response: Only respond if the image pertains to human health issues.
2. Clarity of Image: In cases where the image quality impedes analysis, note that certain ascepts are 'Unable to be determined based on the provided image.'
3. Disclaimer: Accompany your analysis with the disclaimer: "consullt with a doctor before making any decisions."

4. Your insights are invaluable in guiding clinical decions, please proceed with the analysis, adhering to structured approach outlined above.

please provide me an output response with these 4 headings Detailed Analysis, Fidings Report, Recommendations and next steps, Treatment suggestions

"""

model = genai.GenerativeModel(model_name="gemini-pro-vision",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

st.set_page_config(page_title="Vital Image Analytics 🐛", page_icon=":robot:")



st.title("Vital Image Analytics")
st.subheader("An application that can help users to identify medical images")
uploaded_file = st.file_uploader("Upload the medical image for analysis", type=["png","jpg","jpeg"])
if uploaded_file:
    st.image(uploaded_file, width=300, caption="Uploaded Medical Image")

submit_button = st.button("Generate the Analysis")

if submit_button:
    image_data = uploaded_file.getvalue()

    image_parts = [
        {
            "mime_type": "image/jpeg",
            "data": image_data
        },
    ]

    prompt_parts = [

        image_parts[0],
        system_prompt,
    ]

    st.title("Here is the analysis based on your image: ")
    st.image(image_data,width = 250)
    response = model.generate_content(prompt_parts)
    st.write(response.text)