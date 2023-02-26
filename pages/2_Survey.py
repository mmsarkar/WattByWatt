import streamlit as st

# About the page
st.title('Energy Survey')
st.write('Answer these questions to get your own personalized tips on how to make the switch to sustainable energy sources!')

st.subheader('Survey:')

#question 1
st.write('What county do you live in?')
countyChoice = st.selextbox('*Choose an option...*', ('Los Angeles', 'Orange', 'Riverside'))

#question 2
st.write('How many people are in your househoold?')
householdNumber = st.number_input('*Choose a number...*', min_value = 1, max_value = 10, value = int, step = 1)

#question 3
st.write('Which of the following would you like to implement in the future?')
selectedActions = st.multiselect('*Select an option/options...*', ['Solar Panels', ''])

#results from buttons: