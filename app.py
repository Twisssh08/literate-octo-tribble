import streamlit as st
from PIL import Image

st.title("Mi primera app!!")

st.header("HOLY MOLY !!")
st.write("raise your ya ya ya !")
image = Image.open("HolyMoly.jpg")

st.image(image, caption="holyyy god, this is a image")
