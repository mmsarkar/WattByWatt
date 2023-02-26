import streamlit as st

st.set_page_config(page_title="Watt-by-Watt", layout= "wide")

# The Welcmome Page

pics = {
    "Watt By Watt": "https://img.freepik.com/premium-vector/good-idea-banner-light-bulb-idea-concept-creative-concept-light-bulb-drawn-stock-flat-style-vector-illustration_517145-471.jpg",
    "Watt By Watt": "https://thumbs.dreamstime.com/b/banner-lightbulb-idea-concept-creative-bulb-sign-drawn-innovations-background-stock-vector-186875325.jpg",
}
pic = st.selectbox(" ", list(pics.keys()), 0)
st.image(pics[pic], use_column_width=True)

st.title("Home")
st.subheader("*Watt by Watt*, where the economy meets sustainability.")

st.markdown('#')

pics = {
    "Who are we?": "https://media.istockphoto.com/id/1218614876/photo/looking-up-a-reflections-on-glass-covered-corporate-building.jpg?s=612x612&w=0&k=20&c=5wtXtsyFMpENLXr-Kkfz5GnCXP2Av_XfFFxDIfFlVNk=",
    "Who are we?": "https://t3.ftcdn.net/jpg/01/75/82/00/360_F_175820028_Z2Mopy2hTh309ZtMTtB3JptUd6fxoxZE.jpg",
}
pic = st.selectbox(" ", list(pics.keys()), 0)
st.image(pics[pic], use_column_width=True)

st.subheader("What is *Watt by Watt*?")
st.write("We care about making the earth a better place and the first step to this is using our resources wisely. Energy, specifically electricity, combines a plethora of gasses and other non-renewable resources. According to the *California Energy Commission*, in 2021, around 50 percent of the total power in the state of California was generated from nonrenewable sources like coal, natural gas, and oil.")
st.write("We want the data to reflect the truth -- that it is smarter financially and more sustainable to invest in alternate energy sources, starting with solar.")

st.markdown("#")

pics = {
    "How much energy do you use?": "https://images.squarespace-cdn.com/content/v1/5877e86f9de4bb8bce72105c/1503944575877-1TFZYC83OGP8CKLNEOYC/carbon-footprint_med.jpeg",
    "How much energy do you use?": "https://www.enelgreenpower.com/content/dam/enel-egp/immagini/learning-hub/transizione-energetica/rinnovabili_transizione_2400x1160.jpg"
}
pic = st.selectbox(" ", list(pics.keys()), 0)
st.image(pics[pic], use_column_width=True)

st.subheader("Your Energy Footprint.")
st.write("You've probably heard of your carbon footprint. But have you heard of your *energy* footprint?")
st.write("Electricity affects everything and is affected by everything, from the cars you drive to the lights in your house to things we might not think about, like the pipes leading clean water to your shower. Reducing your energy footprint can help every aspect of our global community.")

st.markdown("#")

pics = {
    "Financial Accessibility": "https://i0.wp.com/www.luamaralstudio.com/wp-content/uploads/2022/11/Baddie-aesthetic-images-for-wall-collage-lu-amaral-studio-26.jpg?fit=800%2C1136&ssl=1",
    "Financial Accessibility": "https://static.vecteezy.com/system/resources/thumbnails/007/642/012/small/animation-of-graph-trending-upwards-white-arrow-pointing-up-on-graph-with-blue-light-effect-on-black-background-free-video.jpg",
}
pic = st.selectbox(" ", list(pics.keys()), 0)
st.image(pics[pic], use_column_width=True)

st.subheader("Your Financial Accessibility.")
st.write("Sustainability doesn't have to be unattainable. At *Watt by Watt*, we strive to give all the best information about solar solutions to help make your life easier and the world a better place at the same time, all at a real, affordable price.")
st.write("According to the *U.S. Chamber of Commerce Global Energy Institute*, California has some of the highest U.S. electricity retail prices. Want to lower your bill? Explore our site, and you'll find out! We believe that providing a seamless access to information that can help people make decisions about solar and which solutions work for them can help us take those steps to be a better global community.")
st.write("We offer all the information about savings gotten from solar, but we also are transparent with the one-time costs of the solutions we provide.")


st.markdown('#')

pics = {
    "How to use:": "https://cdn.pixabay.com/photo/2020/05/28/01/25/skyline-5229452_960_720.jpg",
    "How to use:": "https://static.vecteezy.com/system/resources/previews/002/093/076/non_2x/modern-city-skyline-sunset-landscape-backgrounds-illustration-eps10-vector.jpg",
}
pic = st.selectbox(" ", list(pics.keys()), 0)
st.image(pics[pic], use_column_width=True)

st.subheader("How To Use *Watt by Watt*:")
st.write("*It's simple.*")
st.write("Head over to the 'Data' tab to check out general data about your region.")
st.write("If you want advice specific to you, head over to the 'Survey' page and take our survey. You'll get information about the financial feasability of our different solutions compared to the general energy usage per household, customized just for your household.")
# Maybe images, or videos, just to make it pretty