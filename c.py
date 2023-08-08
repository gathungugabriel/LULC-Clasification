
import streamlit as st
import pandas as pd
import folium

# Read data from the CSV file
data = pd.read_csv('training_dataset.csv')

# Streamlit app
st.title('Folium Map in Streamlit')

# Create a Folium map centered at the mean of latitudes and longitudes
m = folium.Map(location=[data['Lat'].mean(), data['Lon'].mean()], zoom_start=5)

# Add markers for each point
for index, row in data.iterrows():
    folium.Marker([row['Lat'], row['Lon']], popup=f"Index: {row['system:index']}<br>Classification: {row['classification']}").add_to(m)

# Display the map using Streamlit
st.write('Map with Markers:')
stfolium = st.empty()
stfolium.map(m)
