import streamlit as st
from PIL import Image

set_mod = ""
st.title("Mi primera app!!")

st.header("HOLY MOLY !!")
st.write("raise your ya ya ya !")
image = Image.open("HolyMoly.jpg")

st.image(image, caption="holyyy god, this is a image")

texto = st.text_input("Put anything here", "Omaigo")
st.write("El texto escrito es...", texto)

st.subheader("ILL PUT 2 COLUMNS THERE!!")

col1, col2 = st.columns(2)

with col1:
  st.subheader("This is my first column, Holy moly!!")
  st.write("this column is ubicated on the left of my page?")
  resp = st.checkbox("Yes sir")
  if resp:
    st.write("We are on the right side!!")

with col2:
  st.subheader("Is this already my SECOND column!??!!")
  modo = st.radio("Wich kind of interface u want?", ("Visual", "Audítive", "Touch"))
  if modo == "Visual":
    st.write("Look up there!!")
  if modo == "Audítive":
    st.write("HEAR ME OUT")
  if modo == "Touch":
    st.write("TOUCH ME AND EXPLORE ME")

st.subheader("THESE ARE MY FIRST BUTTONS")
if st.button("PRESS HERE IF U WANT AN AMAZING REWARD"):
    st.write("WAAAA, U WERE TROLLED")
    image = Image.open("STFU.png")
    st.image(image)
else:
    st.write("PRESS ME PLEASE :,(")

st.subheader(" ARE THESE SELECTBOXES?!")
in_mod = st.selectbox(
  "SELECT A MODALITY",
  ("Auditive", "Visual", "Haptic"),
)
if in_mod == "Audítive":
    set_mod = "IMAGINE A SOUND.... WAIT THERE"
elif in_mod == "Visual":
    set_mod = "REPRODUCIN A VIDEO... WAIT THERE"
elif in_mod == "Haptic":
    set_mod = "ACTIVATIN VIBRATION !!!"
st.write("THE ACTION IS... ", set_mod)

with st.sidebar:
  st.subheader("WOOOP AND WIIIP")
  
  
                  
  

