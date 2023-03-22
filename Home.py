import streamlit as st

import geopandas
import streamlit as st
import numpy as np

import plotly.express as px
import glob

#df_init = pd.read_csv('bike-sharing_hourly.csv')

  
from PIL import Image
st.set_page_config(
    page_title="Real-Time Data Dashboard",
    page_icon="Active",
    layout="wide"
)


# Include the Bootstrap stylesheet in the head section of the Streamlit app
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" crossorigin="anonymous">', unsafe_allow_html=True)

# Define the navbar as a function
# image = Image.open('image.png')

def navbar():
	st.markdown(""" <style>.navbar-brand{padding-top: 50px;}</style>

    <nav class="navbar navbar-expand-lg navbar-dark navbar navbar-dark bg-dark fixed-top" style="height: 120px;">
    	<a class = "navbar-brand" href="#"><img src="" width="320p"></a>
    	<a class="navbar-brand" href="#">Bike Sharing</a>
    	<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    		<span class="navbar-toggler-icon"></span>
  		</button>
  		<div class="collapse navbar-collapse" id="navbarNav">
    		<ul class="navbar-nav">
      			<li class="nav-item active" >
        			<a class="navbar-brand" class="nav-link"  href="http://localhost:8501">Dashboard <span class="sr-only">(current)</span></a>
      			</li>
      			<li class="nav-item">
        			<a  class="navbar-brand"class="nav-link" href="">Source Code</a>
      			</li>
      			<li class="nav-item">
        			<a class="navbar-brand" class="nav-link" href="http://localhost:8501/Modelling">Modelling</a>
      			</li>
      			<li class="nav-item">
        			<a class="navbar-brand" class="nav-link" href="http://localhost:8501/About_Us">Contact us</a>
      			</li>                
      			<li class="nav-item dropdown">
      				<a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Dropdown</a>
      				<div class="dropdown-menu" aria-labelledby="navbarDropdown">
          				<a class="dropdown-item" href="#">Action</a>
          				<a class="dropdown-item" href="#">Another action</a>
          				<div class="dropdown-divider"></div>
          				<a class="dropdown-item" href="#">Something else here</a>
        			</div>
      			</li>
      		</ul>
  		</div>
         
    </nav>
    """, unsafe_allow_html=True)

# Call the navbar function in your Streamlit app


navbar()




st.title("Pedaling Forward")
st.write("Data-driven analysis to improve bike sharing in :blue[Washington, D.C.] using data from :blue[2011] & :blue[2012]")

#  --------------------- insert here ---------------------------------------------------
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from pycaret.regression import *
from sklearn.metrics import r2_score
import pickle
from datetime import datetime

#bike_df = pd.read_csv('bike-sharing_hourly.csv') #profile = True to get the insights
from pycaret.datasets import get_data
bike_df = get_data('bike-sharing_hourly', profile=False)



import time
import streamlit as st
import streamlit as st

st.title("Bike Analysis")

bike_df["Working_Hours"] = np.where((bike_df["workingday"] == 1) & (bike_df["hr"] >= 8) & (bike_df["hr"] <= 17), 1 , 0)
bike_df["Sleeping_Hours"] = np.where(((bike_df["hr"] <= 6) | (bike_df["hr"] >= 23)), 1 , 0)
bike_df["hum_temp_ratio"] = bike_df["hum"] / bike_df["temp"]
bike_df_data = bike_df.drop(columns = ["casual", "registered"], axis = 1)

data = bike_df_data[(bike_df_data["dteday"] >= '2011-01-01') & (bike_df_data["dteday"] < '2012-08-01')]
data_unseen = bike_df_data[(bike_df_data["dteday"] >= '2012-08-01')]

data.reset_index(inplace=True, drop=True)
data_unseen.reset_index(inplace=True, drop=True)

def get_season(date):
    """
    Returns the season of the given date (a datetime object)
    """
    if date.month in [3, 4, 5]:
        return 1
    elif date.month in [6, 7, 8]:
        return 2
    elif date.month in [9, 10, 11]:
        return 3
    else:
        return 4
    
def get_weathersit(weather):
    """
    Returns the season of the given date (a datetime object)
    """
    if weather == 'Clear, Few clouds':
        return 1
    elif weather == 'Mist, Cloudy':
        return 2
    elif weather == 'Light Snow/Rain':
        return 3
    else:
        return 4

# Define the Streamlit app
def main():
    model = load_model(model_name="cnt_bikes")
    
    st.subheader("Predict how many Bikes will you need!" )
    col1, col2, col3 = st.columns(3)
    # Ask the user to input the date as a string
    with col1: 
        day = st.text_input('Enter the date in the format YYYY-MM-DD', '2013-11-20')
        hour = st.number_input('Enter the hour (0-23)', min_value=0, max_value=23, value=15)
        holiday_options = ["No", "Yes"]
        holiday = st.selectbox("Is it a holiday?", options=holiday_options, index=0)
    # Ask the user to input the hour as a number
    with col2:
        weather_options = ['Clear, Few clouds', 'Mist, Cloudy', 'Light Snow/Rain' ,'Thunderstorm, Heavy Rain/Snow']
        weather = st.selectbox("Enter how's the weather ", options=weather_options, index=0)
        temp = st.number_input('Enter the temperature in Celsius', value=21)
        atemp = st.number_input('Enter the feels-like temperature in Celsius', value=17)
    # Ask the user to input the holiday as a number (0 or 1)
    with col3:
        hum = st.number_input('Enter the humidity in percentage', value=30)
        windspeed = st.number_input('Enter the windspeed in km/h', value=5)
   
    
    dteday = datetime.strptime(day, '%Y-%m-%d')
    weekday = dteday.weekday()
    workingday = np.where((weekday <= 4) & (holiday == 0), 1 , 0)
    windspeed = 20
    Working_hours = np.where((workingday == 1) & (hour >= 8) & (hour <= 17), 1 , 0)
    Sleeping_hours = np.where(((hour <= 6) | (hour >= 23)), 1 , 0)
    temp = temp / 41
    atemp = atemp  / 50
    hum = hum / 100
    windspeed = windspeed / 67
    yr = dteday.year
    yr = yr - 2011
    mnth = dteday.month
    hum_temp_ratio = hum / temp
    season = get_season(dteday)
    holiday = np.where((holiday == "Yes") , 1 ,0)
    weathersit = get_weathersit(weather)
    
    data_new = {
    'dteday' : [dteday],
    'season' : [season],
    'yr': [yr],
    'mnth': [mnth],
    'hr': [hour],
    'holiday': [holiday],
    'weekday' : [weekday],
    'workingday': [workingday],
    'weathersit': [weathersit],
    'temp': [temp],
    'atemp': [atemp],
    'hum': [hum],
    'windspeed': [windspeed],
    'Working_Hours': [Working_hours],
    'Sleeping_Hours': [Sleeping_hours],
    'hum_temp_ratio': [hum_temp_ratio]
    }

    df = pd.DataFrame(data_new)
    new_predictions = predict_model(model, data=df)
    pred = new_predictions.iloc[0,16].round()
    
    st.markdown(f"<h1 style='text-align: center;'>You need <u>{pred}</u> bicycles</h1>", unsafe_allow_html=True)






if __name__ == "__main__":
    main()