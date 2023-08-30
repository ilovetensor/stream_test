import streamlit as st
import pandas as pd

st.title('Distance Predictor')

la = st.slider("Choose LA",-50,50)

ev = st.slider("Choose EV",0,100)

release_speed = st.slider("Choose Release Speed",60,110)

fav_platoon_split_for_batter = st.selectbox("Good Platoon Split?", [0,1])

game_elevation = st.slider("Choose Game Elevation",20,7349) 

pull_percent =  st.slider("Choose Pull %",0,100)




# with st.sidebar:
#     add_radio = st.radio(
#         "Choose a shipping method",
#         ("Standard (5-15 days)", "Express (2-5 days)")
#     )


# options = df["EV"].dropna().tolist()
# player = st.selectbox('Player', options)
