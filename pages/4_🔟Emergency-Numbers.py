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

# Add SOS button
if st.button("SOS"):
    # Assuming you want to display the first ambulance number when SOS is clicked
    st.write(f"Call: [{ambulance_numbers[0]['number']}](tel:+91{ambulance_numbers[0]['number']})")
    
# Display ambulance numbers
st.title("Ambulance Numbers")
for ambulance in ambulance_numbers:
    st.markdown(f"**{ambulance['name']}**")
    st.write(f"Call: [{ambulance['number']}](tel:+91{ambulance['number']})")


