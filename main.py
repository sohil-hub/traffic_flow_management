""""This is main file to run the web app"""

# import necessary modules
import streamlit as st
import home, prediction

st.sidebar.title("Navigation")
user_choice = st.sidebar.radio('Go to', ("Home", "Predict"))

# Open the page selected by the user.
if (user_choice == "Predict"): 
    prediction.app()
# elif (user_choice == "About me"):
#     about.app()
else:
    home.app()