import streamlit as st

def main():
    st.title("Feedback Form for MedAI Emergency Response System")

    st.write("We value your feedback to improve our emergency response system. Please take a moment to share your thoughts.")

    # User input fields
    name = st.text_input("Name:")
    email = st.text_input("Email:")
    feedback_type = st.radio("Type of Feedback:", ("General Feedback", "Bug Report", "Feature Request", "Other"))
    feedback_details = st.text_area("Please provide details of your feedback:")

    # Submit button
    if st.button("Submit"):
        # Saving feedback to database or file
        save_feedback(name, email, feedback_type, feedback_details)
        st.success("Thank you for your feedback! We appreciate your input.")

def save_feedback(name, email, feedback_type, feedback_details):
    # Code to save feedback to database or file
    pass

if __name__ == "__main__":
    main()