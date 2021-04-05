# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 13:39:33 2021

@author: admin
"""

# -*- coding: utf-8 -*-
#"""Weather.ipynb
#Automatically generated by Colaboratory.
#Original file is located at
#    https://colab.research.google.com/drive/1j2KV078KZgtld37aeGstl2pRGu2I25FA
#"""

#pip install pyowm streamlit datetime pytz

import os
import pytz
import pyowm
import streamlit as st
import numpy as np
from matplotlib import dates
from datetime import datetime
from matplotlib import pyplot as plt
import requests, json

owm=pyowm.OWM('your-api-key')
mgr=owm.weather_manager()
api_key = "Your_API_Key"

st.title("Weather App")
st.write("Made by Bhargavi :)")
st.write("### Write the name of a City to know the weather there")

place=st.text_input("Enter the city name :","")

if place == "":
    st.write("Input a CITY!")
st.button("submit")
os._exit(0)
st.stop()
#unit=st.selectbox("Select Temperature Unit",("Celsius","Fahrenheit"))

#g_type=st.selectbox("Select Graph Type",("Line Graph","Bar Graph"))
import time
base_url = "http://api.openweathermap.org/data/2.5/weather?"
complete_url = base_url + "appid=" + api_key + "&q=" + place
response = requests.get(complete_url)
  
# Enter your API key here
api_key = "dd1a9be51e2fb72d243de4e4fc388f54"
  
# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"
  
# Give city name
city_name = place
  
# complete_url variable to store
# complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
  
# get method of requests module
# return response object
response = requests.get(complete_url)
  
# json method of response object 
# convert json format data into
# python format data
x = response.json()
  
# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
if x["cod"] != "404" or " ":
    # store the value of "main"
    # key in variable y
    y = x["main"]
    # store the value corresponding
    # to the "temp" key of y
    current_temperature = y["temp"]
  
    # store the value corresponding
    # to the "pressure" key of y
    current_pressure = y["pressure"]
  
    # store the value corresponding
    # to the "humidity" key of y
    current_humidity = y["humidity"]
  
    # store the value of "weather"
    # key in variable z
    z = x["weather"]
  
    # store the value corresponding 
    # to the "description" key at 
    # the 0th index of z
    weather_description = z[0]["description"]
  
    # print following values
    st.write(" Temperature (in Celsius) = ",(current_temperature-273)," Celsius")
    st.write("atmospheric pressure (in hPa unit) = ",current_pressure)
    st.write(" humidity (in percentage) = ",current_humidity, "%")
    st.write(" description = ",weather_description)
elif  place == " ":
    st.subheader(" ")
#else:
    #st.subheader(" City Not Found ")
