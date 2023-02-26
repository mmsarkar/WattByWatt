import streamlit as st
from PIL import Image
# import os

st.set_page_config(page_title="About Us", layout= "wide")
# our mission
st.title("Our Mission")
st.write('We believe the road to sustainability is a straight path, filled with the convolution of road blocks in the forms of high prices, low incentives, and many other obstacles. We want to set the record straight with the power of data, creating a central resource for those interested in reducing their energy footprint. Our goal is to show consumers the power they hold in the energy consumption and of the alternatives available to them, and hopefully make the world a cleaner place as a result.')

# team members
st.title("Our Team")
# team member: Medha
# files = os.listdir('medhaheadshot')
# for file in files:
#     img = Image.open(os.path.join('WattByWatt', file))
image = Image.open("medhaheadshot.jpg")
st.image(image)
st.subheader('Medha Sarkar')
st.write('Medha is a second-year Economics major with a Computer Science minor who splits her time between learning new data visulaization/cleansing softwares and techniques, mentoring business students in career development workshops, and working on a music production capstone project.')
st.write('She is interested in data analytics and consulting, and in the future would like to be a strategy or technology consultant, and become an expert with data, bridging the gap between data and business processes.')


# team member: MJ
st.subheader('Madison Juliana Oliva (she/her)')
st.write('MJ is a second-year computational mathematics major with an interest for machine learning and data structures. She nurtures her love for number theory and combinatorics through engaging meetings with her peers in the Math Club.')
st.write('MJ also gets involved with professors and graduate students research in fields including machine learning for exposure and to work towards her capstone project. Her career goals are to enter the technology industry to create apps or even building a data processor sometime in the future.')