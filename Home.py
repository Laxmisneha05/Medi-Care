import streamlit as st

st.set_page_config(
    page_title="Medi-Care AI",
    page_icon="🏥🏥"
)

# Function to display information about heart attack
def heart_attack_page():
    st.title("Heart Attack")
    st.write("Watch this video to learn more about heart health:")
    st.write('<iframe width="560" height="315" src="https://www.youtube.com/embed/N9yUmduG820" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', unsafe_allow_html=True)
    st.write("A heart attack occurs when the flow of blood to the heart is blocked.")
    st.write("Symptoms:")
    st.write("- Chest pain or discomfort")
    st.write("- Shortness of breath")
    st.write("- Nausea or lightheadedness")
    st.write("Prevention:")
    st.write("- Maintain a healthy weight")
    st.write("- Eat a balanced diet low in saturated fats")
    st.write("- Exercise regularly")
    st.write("- Avoid smoking and excessive alcohol consumption")

# Function to display information about high blood pressure
def high_blood_pressure_page():
    st.title("High Blood Pressure")
    st.write("Watch this video to learn more about heart health:")
    st.write('<iframe width="560" height="315" src="https://www.youtube.com/embed/D1bg5NSpRoI" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', unsafe_allow_html=True)
    st.write("High blood pressure, or hypertension, is a condition where the force of the blood against the artery walls is too high.")
    st.write("Symptoms:")
    st.write("- Headaches")
    st.write("- Dizziness")
    st.write("- Blurred vision")
    st.write("Prevention:")
    st.write("- Reduce salt intake")
    st.write("- Maintain a healthy diet")
    st.write("- Exercise regularly")
    st.write("- Limit alcohol consumption")

# Function to display information about cancer
def cancer_page():
    st.title("Cancer")
    st.write("Watch this video to learn more about heart health:")
    st.write('<iframe width="560" height="315" src="https://www.youtube.com/embed/BttAtBZeQc4" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', unsafe_allow_html=True)
    st.write("Cancer is a disease characterized by the uncontrolled growth and spread of abnormal cells.")
    st.write("Symptoms:")
    st.write("- Lump or thickening in the breast or other parts of the body")
    st.write("- Persistent cough or hoarseness")
    st.write("- Changes in bowel or bladder habits")
    st.write("Prevention:")
    st.write("- Avoid tobacco use")
    st.write("- Limit exposure to sunlight")
    st.write("- Eat a healthy diet rich in fruits and vegetables")
    st.write("- Get regular screenings")

# Main page
st.title("Medi-Care AI")
page = st.sidebar.selectbox("Select a page", ["Main Page", "Heart Attack", "High Blood Pressure", "Cancer"])

if page == "Main Page":
    st.write("Welcome to Medi-Care AI. Select a disease from the sidebar to learn more about it.")
    st.image("ex.png", caption="Your Personalized Ai Assistant 🚒", use_column_width=True)
elif page == "Heart Attack":
    heart_attack_page()
elif page == "High Blood Pressure":
    high_blood_pressure_page()
elif page == "Cancer":
    cancer_page()
