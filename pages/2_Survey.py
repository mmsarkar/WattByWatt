import streamlit as st
import pandas as pd
import numpy as np
import gspread
from gspread_dataframe import get_as_dataframe, set_with_dataframe

# About the page
st.title('Energy Survey')
st.write('Answer these questions to get your own personalized tips on how to make the switch to sustainable energy sources!')

st.subheader('Survey:')
isFinished = False
#question 1
st.write('What county do you live in?')
countyChoice = st.selectbox('*Choose an option...*', ('Los Angeles', 'Orange', 'Riverside'))

#question 2
st.write('How many people are in your househoold?')
householdNumber = st.number_input('*Choose a number...*', min_value = 1, max_value = 10, value = 1, step = 1)

#question 3
st.write('Which of the following would you like to try or learn more about?')
selectedActions = st.multiselect('*Select an option/options...*', ['Solar Panels', 'Sustainable Transportation', 'Eco-Driving', 'Sustainable Shower Heads'])

#Done button:
st.write('Click the button to complete the survey!')
isFinished = st.button('Done?')

gc = gspread.service_account(filename='/Users/mj/Desktop/WATTSSSS/WattByWatt/.venv/lib/python3.11/site-packages/gspread/watt-by-watt-database-abb4a6c70d6c.json')
sh = gc.open("WattByWatt")
worksheet = sh.worksheet('AverageEnergyUsage')

#results from buttons:
if isFinished == True:
    if (countyChoice == 'Los Angeles'):
        lacEnergyOne = float(worksheet.acell('B6').value)
        lacEnergyHome = lacEnergyOne * householdNumber
        st.write('In L.A. county, the typical energy usage of an individual is ', lacEnergyHome, ' kilowatt hours.')
        st.write ('For your household of ', householdNumber, ' the estimated energy usage is ', lacEnergyHome, ' kilowatt hours.')
        st.write('You selected: ', selectedActions)

    if (countyChoice == 'Orange'):
        ocEnergyOne = float(worksheet.acell('C6').value)
        ocEnergyHome = ocEnergyOne * householdNumber
        st.write('In Orange county, the typical energy usage of an individual is ', ocEnergyHome, ' kilowatt hours.')
        st.write ('For your household of ', householdNumber, ' the estimated energy usage is ', ocEnergyHome, ' kilowatt hours.')
        st.write('You selected: ', selectedActions)

    if (countyChoice == 'Riverside'):
        rcEnergyOne = float(worksheet.acell('D6').value)
        rcEnergyHome = rcEnergyOne * householdNumber
        st.write ('In L.A. county, the typical energy usage of an individual is ', lacEnergyHome, ' kilowatt hours.')
        st.write ('For your household of ', householdNumber, ' the estimated energy usage is ', lacEnergyHome, ' kilowatt hours.')
        st.write('You selected: ', selectedActions)

st.subheader('Interested in more sustainable practices?')
st.write('Check out our "Data" page for more information!')

