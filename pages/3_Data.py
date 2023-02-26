import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Energy and Finance Data", layout= "wide")

# Intro to page
st.title('Energy and Finance Compendium')
st.subheader("*Where environmentalists meet economists!*")
st.write("Here, you can find different lists and charts detailing the environmental impacts and financial accessibility of sustainable practices.")

# List 1: Average Energy Usage
st.subheader('Average Energy Usage')
st.write('Calculating the energy usage of households and individuals depending on county! Select an option below to begin.')

countySelect = st.selectbox(
       "Choose a county:", 
       ("Los Angeles", "Orange", "Riverside"),)

#list 1.1
if countySelect == "Los Angeles":
    st.subheader("Los Angeles County")
#list 1.2  
if countySelect == "Orange":
    st.subheader("Orange County")
#list 1.3
if countySelect == "Riverside":
    st.subheader("Riverside County")
    