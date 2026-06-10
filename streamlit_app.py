import streamlit as st
from pathlib import Path

#Page settings
st.set_page_config(
    page_title="School Events App",
    page_icon="📅",
    layout="wide"
)

# Logo
logo_path = Path(__file__).parent / "logo.png"
st.image(str(logo_path), width=200)

#Title
st.title("Welcome to the School Events App")

#Description
st.write("""
         This application allows parents, students, teachers,
         and staff members to view upcoming school events
         and register for events happening on campus.
         
         Select your role below to get started.
         """)