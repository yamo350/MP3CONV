import pytube
import os
import streamlit as st
import time
from pytube import YouTube

st.set_page_config(page_title='Youtube Converter',
                   page_icon='🐳',
                   layout="centered",
                   initial_sidebar_state="auto",
                   menu_items={
                     'Get help':'https://www.facebook.com/share/ubY7H5PdGuYXxCPo/?mibextid=WC7FNe','Report a bug': "https://www.facebook.com/share/ubY7H5PdGuYXxCPo/?mibextid=WC7FNe",'About': "# This is just a small project i made lol. If you want to improvise click the above links"})
file = st.text_input("Enter a valid Youtube URL😊")
try:
 
  if st.button('DOWNLOAD MP4🐳'):
     with st.spinner("Just be a little patient 🐳🐳🐳"):
       time.sleep(5)
     video = YouTube(file)
     video.streams.filter(progressive=True,
                          file_extension='mp4').order_by('resolution').desc().first().download(output_path="C:\\Users\\Student\\Downloads")
     st.write('MP4 Successfully downloaded👌')


except FileExistsError :
    st.write("FILE ALREADY EXIST DUMBASS CHECK YOUR DOWNLOADS")


if st.button("TO ACCESS FILE LOCATION") :
    st.write("Go to your Downloads **STUPID** 💩")
with st.sidebar:
  st.write("# IttsKwestaa❤️")
  st.write("[SHOW SOME LOVE AND LIKE>](https://www.facebook.com/share/ubY7H5PdGuYXxCPo/?mibextid=WC7FNe)")
  st.write("[For more projects>](https://calculatorforbaya-h3hmvab2tdwsvcu7pcas8b.streamlit.app/)")

     


