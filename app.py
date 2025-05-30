import streamlit as st
import requests
import datetime

# Title
st.title("TaxiFareModel front")

# Instructions
st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

d = st.date_input(
    "When's",
    datetime.date(2014, 7, 6))
st.write('Your date  is:', d)
t = st.time_input('Time?', datetime.time(19, 18))
st.write('Time chosen', t)
number0 = st.number_input('Insert a pickup longitude',-73.950655)
st.write('The current pickup longitude is ', number0)
number1 = st.number_input('Insert a pickup latitude',40.783282)
st.write('The current pickup latitude is ', number1)
number2 = st.number_input('Insert a dropoff longitude',-73.984365)
st.write('The current dropoff longitude is ', number2)
number3 = st.number_input('Insert a dropoff latitude',40.769802)
st.write('The current dropoff latitude is ', number3)
number4 = st.number_input('Insert a passenger count',1)
st.write('The current passenger count is ', number4)

# Build parameters dictionary
params = {
          "pickup_datetime": f"{d} {t}",
          "pickup_longitude":number0,
          "pickup_latitude":number1,
          "dropoff_longitude":number2,
          "dropoff_latitude":number3,
          "passenger_count":number4
        }

# Call API and display prediction
if st.button("Get fare prediction"):
    url = 'https://taxifare.lewagon.ai/predict'
    response = requests.get(url, params=params)
    prediction = response.json()
    st.success(f"Estimated fare: ${prediction}")
