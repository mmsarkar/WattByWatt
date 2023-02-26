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
worksheetSol = sh.worksheet('Solutions')

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

# Solutions Section
st.title('Sustainable Solutions')

sd_read = get_as_dataframe(worksheetSol, usecols = [0, 1, 2], nrows = 4)
sd_read

st.write('Click the a button to learn more about those sustainability practices!')
houseFix = st.button('Household')
transportFix = st.button('Transportation')

if houseFix == True:
    st.subheader("Solar Panels")
    st.write("Installing solar panels in your home is a great way to switch your household to a sustainable energy source reducing carbon emmissions. Besides the price tag, there is a certain roof requirements for installations, which you can explore through the link: https://www.energy.gov/eere/solar/homeowners-guide-going-solar.")
    st.subheader("Sustainable Shower Heads")
    st.write("Specifically Aerator shower heads, these shower heads allow larger dropplets of water to go through, therefore creating the feeling of a more pwoerful shower. Doing so reduces the demand for water, using as little as 7.5-20 liters per minute, as opposed to the regular shower heads using up to 30 liters of water per minute. By reducing water usage, and therefore hot water, the energy used for heating the water will be reduced as well! Check this link for more details: https://thebathroomblueprint.com/aerator-shower-head/.")
if transportFix == True:
    st.subheader("Sustainable Cars")
    st.write("As solar panel cars go further in development, they could potentially be a great sustainable tranportation option! In the meantime, switching to electric cars would help reduce carbon emmissions, as well as save money on gas, bridging financial and environmental benefits!")
    st.subheader("Eco-driving")
    st.write("Practicing eco-driving is useful for minimizing fuel consumption and therefore carbon emmisions. Some guidelines to follow include choosing a low-emmision car, avoiding short car trips, close windows while driving, and so on. By conserving the fuel and reucing your usage, you will save gas money! Learn more at this link: http://www.ecodrive.org/en/what_is_ecodriving/")