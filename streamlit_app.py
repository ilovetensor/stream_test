import streamlit as st
import pandas as pd
import joblib

# model = joblib.load('xgbr.joblib')

st.title('Distance Predictor')

la = st.slider("Choose LA",-50,50)
ev = st.slider("Choose EV (MPH)",60,120)
release_speed = st.slider("Choose Release Speed (MPH)",60,110)
fav_platoon_split_for_batter = st.selectbox("Good Platoon Split?", [0,1])
game_elevation = st.slider("Choose Game Elevation ()Feet",20,7349) 
pull_percent =  st.slider("Choose Pull %",0.0,1.0)

# df = pd.read_csv('final_input.csv')

# df['launch_angle'].iloc[0] = la
# df['launch_speed'].iloc[0] = ev
# df['release_speed'].iloc[0] = release_speed
# df['fav_platoon_split_for_batter'].iloc[0] = fav_platoon_split_for_batter
# df['game_elevation'].iloc[0] = game_elevation
# df['pull_percent'].iloc[0] = pull_percent

# p =  model.predict(df)

# st.title(p[0])

