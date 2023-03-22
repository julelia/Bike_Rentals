

import hydralit_components as hc
import pandas as pd

import geopandas
import streamlit as st
import numpy as np
import plotly.graph_objects as go

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
        			<a class="navbar-brand" class="nav-link"  href="http://localhost:8501/">Dashboard <span class="sr-only">(current)</span></a>
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
st.title("Exploratory Data Analysis")
st.write("In this analysis, we will explore the trends of bike rentals in 2011 and 2012 using Exploratory Data Analysis techniques, which will allow us to uncover patterns and insights that can inform future bike rental strategies.")
bike_df = pd.read_csv('bike-sharing_hourly.csv')
bike_df = bike_df.rename(columns={'yr': 'Year','hr':'Hour','mnth': 'Month','temp': 'Temperature', 'cnt': 'Count'})


season_map = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
bike_df['season'] = bike_df['season'].replace(season_map)
weekday_map = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
bike_df['weekday'] = bike_df['weekday'].replace(weekday_map)




# Group by
df_date = bike_df.groupby(['dteday']).mean()
df_date = df_date.reset_index()

df_season = bike_df.groupby(['Year','season']).mean()
df_season = df_season.reset_index()

df_weekday = bike_df.groupby(['Year','weekday','Hour']).mean()
df_weekday = df_weekday.reset_index()

df_Year = bike_df.groupby(['Year']).mean()
df_Year = df_Year.reset_index()

df_hr = bike_df.groupby(['Year','Hour']).sum()
df_hr = df_hr.reset_index()

fig = px.line(df_date, x='dteday', y='Count')

fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
st.subheader('Bikes Rented Trends in 2011 & 2012')
st.plotly_chart(fig, use_container_width=True)
col1, col2 = st.columns(2)

with col1:
	input = st.selectbox('Select the year for which you want to see the plots',('2011','2012'))

with col2:
	options = st.multiselect('Which question(s) do you want answered:',['What percentage of users are casual and what percentage are registered?', 
								    								'When are bikes most commonly used?', 
																	'What season sees the highest bike usage?', 
																	'Is there any correlation between bike usage and temperature?', 
																	'Which weekday experiences the highest bike usage?'], ['When are bikes most commonly used?', 
																	'What season sees the highest bike usage?'])




i = 0
if input == '2011':
	i = 0
else:
	i = 1
labels =['casual','registered']
values = [int(df_Year.loc[df_Year.Year == i]['casual']), int(df_Year.loc[df_Year.Year == i]['registered'])]

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
col5, col6 = st.columns(2)
col7, col8 = st.columns(2)
col9, col10 = st.columns(2)

for index in options:
	with col1:
		if index == 'Is there any correlation between bike usage and temperature?':
			fig4 = px.scatter(x=df_date.loc[df_date.Year == i]['Temperature'], y=df_date.loc[df_date.Year == i]['Count'])
			st.subheader("The Impact of Temperature on Bike Usage")
			st.plotly_chart(fig4, use_container_width=True)
	with col2:
		if index == 'Is there any correlation between bike usage and temperature?':
			st.subheader("Insights:")
	with col3:
		if index == 'What percentage of users are casual and what percentage are registered?':
			fig6 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
			st.subheader("Proportion of Casual and Registered Users")
			st.plotly_chart(fig6, use_container_width=True)
	with col4:
		if index == 'What percentage of users are casual and what percentage are registered?':
			st.subheader("Insights:")
	with col5:
		if index == 'When are bikes most commonly used?':
			fig1 = px.line(df_weekday.loc[df_weekday.Year == i], x="Hour", y="Count", color='weekday')
			st.subheader("Hourly/Daily Bike Usage Patterns")
			st.plotly_chart(fig1, use_container_width=True)
	with col6:
		if index == 'When are bikes most commonly used?':
			st.subheader("Insights:")
	with col7:
		if index == 'What season sees the highest bike usage?':
			fig2 = px.bar(df_season.loc[df_season.Year == i], y='Count', x='season', text_auto='.2s')
			st.subheader("Comparison of Bike Usage Across Seasons")
			st.plotly_chart(fig2, use_container_width=True)
	with col8:
		if index == 'What season sees the highest bike usage?':
			st.subheader("Insights:")
	with col9:
		if index == 'Which weekday experiences the highest bike usage?':
			fig5 = px.bar(df_weekday.loc[df_weekday.Year == i], y='Count', x='weekday', text_auto='.2s')
			st.subheader("Comparison of Bike Usage Across Week days")
			st.plotly_chart(fig5, use_container_width=True)
	with col10:
		if index == 'Which weekday experiences the highest bike usage?':
			st.subheader("Insights")


import plotly.graph_objects as go
import pandas as pd

# Define mapbox access token
mapbox_access_token = 'pk.eyJ1IjoibWFoYW1haGFtIiwiYSI6ImNsZmVmbzB5NzBsdzYzdGxycDVrbGhwczkifQ.3tBOuJe1-EeMkkCUJ2BizA'

# Define the center coordinates and zoom level of the map
center_lat = 38.9072
center_lon = -77.0369
zoom = 10

# Define the locations of interest
locations = {
    'Logan Circle': {'lat': 38.9097, 'lon': -77.031978},
    'Navy Yard': {'lat': 38.8765, 'lon': -77.0006},
    'Georgetown': {'lat': 38.909675, 'lon': -77.0654},
    'Capitol hill': {'lat': 38.8860, 'lon': -76.9995},
    'Downtown': {'lat': 38.9037, 'lon': -77.0363},
    'Brightwood': {'lat': 38.9649, 'lon': -77.0277},
    'Northwest Washington': {'lat': 38.9381, 'lon': -77.0449}
}

# Define the color for each neighborhood


# Define the data for the map
data = []
for neighborhood, location in locations.items():
    data.append(go.Scattermapbox(
        lat=[location['lat']],
        lon=[location['lon']],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=20,
            symbol='circle',
            color='rgb(194, 24, 7)',
            opacity=0.8
        ),
        name=neighborhood
    ))

# Define the layout for the map

layout = go.Layout(
    autosize=True,
    hovermode='x',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=center_lat,
            lon=center_lon
        ),
        pitch=0,
        zoom=zoom,
        style='light'
    ),
)

# Create the figure and plot the map
fig = go.Figure(data=data, layout=layout)
fig.update_traces(showlegend=False)
st.subheader("Neighborhoods of Interest in Washington DC")
st.plotly_chart(fig, use_container_width=True)
