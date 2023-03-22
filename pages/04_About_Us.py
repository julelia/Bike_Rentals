import geopandas
import streamlit as st
import numpy as np

import plotly.express as px
import glob

#df_init = pd.read_csv('bike-sharing_hourly.csv')

  
from PIL import Image


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
with st.container():
    st.title("Team Members")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("Maha.png")
        st.text("Maha Hamdi")
        st.markdown("mahahamdi@student.ie.edu", unsafe_allow_html=True)
    with col2:
        st.image("Gustavo.png")
        st.text("Gustavo Welsh")
        st.markdown("gustavo.welsh@student.ie.edu", unsafe_allow_html=True)
    with col3:
        st.image("walid.png")
        st.text("Walid Mneymneh")
        st.markdown("walid.mneymneh@student.ie.edu", unsafe_allow_html=True)
        
    col4, col5, col6 = st.columns(3)
    with col4:
        st.image("Alex.png")
        st.text("Alex García")
        st.markdown("alex.eaton@student.ie.edu", unsafe_allow_html=True)

    with col5:
        st.image("philip.png")
        st.text("Philipp Klement")
        st.markdown("philipp.klement@student.ie.edu", unsafe_allow_html=True)

    with col6:
        st.image("guiermo.png")
        st.text("GuillermoLópez") 
        st.markdown("guillermo.lmd@student.ie.edu", unsafe_allow_html=True)


    col7, col8 = st.columns(2)
    with col7:
        st.image("Julien.png")
        st.text("Julien Elia")  
        st.markdown("julien.elia@student.ie.edu", unsafe_allow_html=True)

