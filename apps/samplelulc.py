import streamlit as st
import pandas as pd
import folium
import leafmap.foliumap as leafmap

def app():
    st.title("LULC Map")

    # Sample DataFrame containing LULC dataset
    data = {
        "latitude": [32.358035, 14.214222, 32.101836, 14.554055, 14.286447],
        "longitude": [48.157335, 33.513448, 48.539927, 33.149720, 33.442751],
        "band1": [4984.333333, 1321.916667, 5159.166667, 513.153846, 1070.291667],
        "band2": [4605.916667, 1165.708333, 4733.250000, 381.846154, 947.708333],
        "band3": [4310.958333, 1089.125000, 4536.291667, 367.846154, 941.166667],
        "class": ["Class A", "Class B", "Class A", "Class C", "Class B"]
    }
    df = pd.DataFrame(data)

    st.write("Preview of the LULC dataset:")
    st.write(df)

    # Create a Folium map centered at the mean of latitudes and longitudes
    center_lat = df['latitude'].mean()
    center_lon = df['longitude'].mean()
    m = leafmap.Map(location=[center_lat, center_lon], zoom_start=10)

    # Add markers for each row in the DataFrame
    for index, row in df.iterrows():
        folium.Marker([row['latitude'], row['longitude']], popup=row['class']).add_to(m)

    # Display the map using Streamlit
    st.write("LULC Map:")
    st.write(m._repr_html_())

# if __name__ == "__main__":
#     app()
