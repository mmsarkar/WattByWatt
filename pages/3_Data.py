import streamlit as st
import pandas as pd
import numpy as np
import gspread
from gspread_dataframe import get_as_dataframe, set_with_dataframe

st.set_page_config(page_title="Energy and Finance Data", layout= "wide")

# Intro to page
st.title('Energy and Finance Compendium')
st.subheader("*Where environmentalists meet economists!*")
st.write("Here, you can find different lists and charts detailing the environmental impacts and financial accessibility of sustainable practices.")

# List 1: Average Energy Usage
st.subheader('Average Energy Usage')
st.write('Select an option below to begin.')

countySelect = st.selectbox(
       "Choose a county:", 
       ("Los Angeles", "Orange", "Riverside"),)

gc = gspread.service_account(filename='/Users/mj/Desktop/WATTSSSS/WattByWatt/.venv/lib/python3.11/site-packages/gspread/watt-by-watt-database-abb4a6c70d6c.json')
sh = gc.open("WattByWatt")
worksheet = sh.worksheet('AverageEnergyUsage')

st.write("Calculating the energy usage of households and individuals depending on county!")


#list 1.1
if countySelect == "Los Angeles":
    st.subheader("Los Angeles County")
    
    #opens the energy usage spreadsheet (google, using Google SHeets API)

    eu_read = get_as_dataframe(worksheet, usecols = [0, 1], nrows = 5)
    eu_read
    #s_range = sh.worksheet("AverageEnergyUsage")
    #for row in s_range:
        #for col in row:
            #print(str(col).rjust(15), end="") # CHECK COLUMN WIDTH
        #print("")

#list 1.2  
if countySelect == "Orange":
    st.subheader("Orange County")
    eu_read = get_as_dataframe(worksheet, usecols = [0, 2], nrows = 5)

    eu_read
#list 1.3
if countySelect == "Riverside":
    st.subheader("Riverside County")
    eu_read = get_as_dataframe(worksheet, usecols = [0, 3], nrows = 5)
    eu_read
