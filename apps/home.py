import streamlit as st
import leafmap.foliumap as leafmap

def app():
    st.title("Home")

    st.markdown(
        """
    HOME FOR LULC
    """
    )

    # Create a Streamlit placeholder to render the map
    map_placeholder = st.empty()
    
    m = leafmap.Map(locate_control=True)
    m.add_basemap("ROADMAP")
    
    # Use the map_placeholder to render the map
    map_placeholder.leaflet(m)

# if __name__ == "__main__":
#     app()
