import streamlit as st
from datetime import date

# Title
st.title("Widgets Playground")

# Input Widgets
name = st.text_input("Name")
age = st.number_input("Age", min_value=1, max_value=100, value=20)
marks = st.slider("Marks", 0, 100, 75)
city = st.selectbox("City", ["Chennai", "Mumbai", "Delhi"])

skills = st.multiselect(
    "Skills",
    ["Python", "ML", "SQL", "Streamlit"]
)

gender = st.radio(
    "Gender",
    ["Male", "Female", "Other"]
)

agree = st.checkbox("I agree to the terms")

dob = st.date_input(
    "Date of Birth",
    date(2000, 1, 1)
)

file = st.file_uploader("Upload a file")

# Submit Button
if st.button("Submit"):
    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Marks:", marks)
    st.write("City:", city)
    st.write("Skills:", skills)
    st.write("Gender:", gender)
    st.write("Agreed:", agree)
    st.write("DOB:", dob)

    if file is not None:
        st.write("File uploaded:", file.name)