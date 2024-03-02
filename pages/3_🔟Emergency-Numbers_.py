import streamlit as st 
st.title("Numbers")

# Define the ambulance numbers
ambulance_numbers = [
    {"number": "9967955239", "name": "Ambulance Number 1"},
    {"number": "9967955239", "name": "Ambulance Number 2"},
    {"number": "9967955239", "name": "Ambulance Number 3"},
    {"number": "9967955239", "name": "Ambulance Number 4"},
    {"number": "9967955239", "name": "Ambulance Number 5"},
]

# Display ambulance numbers
st.title("Ambulance Numbers")
for ambulance in ambulance_numbers:
    st.markdown(f"**{ambulance['name']}**")
    st.write(f"Call: [{ambulance['number']}](tel:+91{ambulance['number']})")
