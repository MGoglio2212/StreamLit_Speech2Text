import os 
os.chdir(r"C:\Users\Gogliom\OneDrive - Jakala SpA\Proposta_SKy\Audio Analysis")


# import library
import streamlit as st
from PIL import Image
import wave
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

import altair as alt

import speech_recognition as sr
import re

# import file

filename_1 = "TEST.wav"
img_logo = Image.open('logo.png')
white_img = Image.open('white.PNG')

######################### STREAMLIT #########################
header = st.beta_container()
sound = st.beta_container()
kpi = st.beta_container()
play = st.beta_container()

st.markdown("""
<style>
.JTALK_1 {font-size:40px !important; font-family: arial black;color: #B41E3C}
.JTALK_2 {font-size:40px !important; font-family: arial black;color: #002060}
.big-font {font-size:30px !important; font-family: arial black;color: #002060}
.medium-font {font-size:20px !important; font-family: arial black;color: #002060}
.small-font {font-size:15px !important; font-family: arial;color: #000000}
</style>
""", unsafe_allow_html=True)

# side bar
st.sidebar.image(img_logo, width = 180)
example = st.sidebar.selectbox("Select a file ", ['None','Example 1', 'Example 2'])

# analyze the file
if example == "Example 1":
    filename = filename_1

spf = wave.open(filename, "r")
signal = spf.readframes(-1)
signal = np.fromstring(signal, "Int16")
fs = spf.getframerate()
time = np.linspace(0, len(signal) / fs, num=len(signal))
df = pd.DataFrame({'time':time, 'signal':signal})

# text from audio
r = sr.Recognizer()
with sr.AudioFile(filename) as source:
    audio_data = r.record(source)
    text_audio = r.recognize_google(audio_data)
    wordList = re.sub("[^\w]", " ",  text_audio).split()

######################### INTRO #########################
with header:
    st.markdown('<div style="text-align:center"><span class="JTALK_1">J</span><span class="JTALK_2">AKALA - Customer Operation</span></div>', unsafe_allow_html=True)
    st.image(white_img, width = 25)

######################### AUDIO #########################
with sound:
    st.markdown('<div style="text-align:center"><p class="big-font">Process Mining of an IVR</p></div>', unsafe_allow_html=True)  
    st.image(white_img, width = 25)

    but1, but2, but3, but4, but5 = st.beta_columns(5)

    # chart = alt.Chart(df).mark_line().encode(x='time', y='signal', color='key:N')
    # st.altair_chart(chart)
    
    if (but3.button("CALCULATE")):
        st.image(white_img, width = 25)

        plt.figure(figsize=(35,10))
        plt.title("Signal Wave", fontsize=30)
        plt.xlabel('Time', fontsize=24)
        plt.ylabel('Frequency', fontsize=24)
        plt.xticks(fontsize=20)
        plt.yticks(fontsize=20)
        plt.plot(time, signal)
        st.pyplot(plt)

        st.image(white_img, width = 25)

        st.markdown('<div style="text-align:center"><p class="medium-font">KPI Registered</p></div>', unsafe_allow_html=True)  
        
        kpi1_col, kpi2_col = st.beta_columns(2)
        
        # First column
        kpi1_col.markdown('<div style="text-align:left"><p class="medium-font">General Overview</p></div>', unsafe_allow_html=True)
        kpi1_col.markdown('<div style="text-align:left"><p class="small-font">Total length:</p></div>', unsafe_allow_html=True)
        kpi1_col.write(time[-1])
        kpi1_col.markdown('<div style="text-align:left"><p class="small-font">Number of words:</p></div>', unsafe_allow_html=True)
        kpi1_col.write(len(wordList))
        kpi1_col.markdown('<div style="text-align:left"><p class="small-font">Number of sentences:</p></div>', unsafe_allow_html=True)
        kpi1_col.write('6')

        # Second column
        kpi2_col.markdown('<div style="text-align:left"><p class="medium-font">Conversation details:</p></div>', unsafe_allow_html=True)
        kpi2_col.markdown('<div style="text-align:left"><p class="small-font">Welcome speech:</p></div>', unsafe_allow_html=True)
        kpi2_col.write('10 sec')
        kpi2_col.markdown('<div style="text-align:left"><p class="small-font">Commercial speech:</p></div>', unsafe_allow_html=True)
        kpi2_col.write('20 sec')
        kpi2_col.markdown('<div style="text-align:left"><p class="small-font">Option list:</p></div>', unsafe_allow_html=True)
        kpi2_col.write('24 sec')
        kpi2_col.markdown('<div style="text-align:left"><p class="small-font">Repeating answer:</p></div>', unsafe_allow_html=True)
        kpi2_col.write('13 sec')

    st.image(white_img, width = 25)

######################## PLAY AUDIO #########################
with play:
    st.markdown('<div style="text-align:center"><p class="big-font">Play the Audio</p></div>', unsafe_allow_html=True)  
    audio_file = open(filename, 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes)

    st.image(white_img, width = 25)
    but1, but2, but3, but4, but5 = st.beta_columns(5)
    if (but3.button("SPEECH")):
        st.image(white_img, width = 25)
        st.write(text_audio)