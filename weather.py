# -*- coding: utf-8 -*-
"""Weather.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1j2KV078KZgtld37aeGstl2pRGu2I25FA
"""

!pip install pyowm streamlit datetime pytz

import os
import pytz
import pyowm
import streamlit as st
from matplotlib import dates
from datetime import datetime
from matplotlib import pyplot as plt

owm=pyowm.OWM('your-api-key')
mgr=owm.weather_manager()

st.title("5 Day Weather Forecast")
st.write("### Write the name of a City and select the Temperature Unit and Graph Type from the sidebar")

place=st.text_input("NAME OF THE CITY :", "")

if place == None:
    st.write("Input a CITY!")

unit=st.selectbox("Select Temperature Unit",("Celsius","Fahrenheit"))

g_type=st.selectbox("Select Graph Type",("Line Graph","Bar Graph"))
