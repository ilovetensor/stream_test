import streamlit as st
import pandas as pd
import joblib

#joblib now imports but wtf no model........
#model = joblib.load('xgbr.joblib')

st.title('Distance Predictor')

la = st.slider("Launch Angle",0,50, index=25)
ev = st.slider("Exit Velocity",0,120)
release_speed = st.slider("Release Speed",60,110)
fav_platoon_split_for_batter = st.slider("Favorable Batter Platoon Split", 0,1)
game_elevation = st.slider("Game Elevation",20,7349) 
pull_percent =  st.slider("Pull %",0.0,1.0)

df = pd.read_csv('final_input.csv')

df['launch_angle'].iloc[0] = la
df['launch_speed'].iloc[0] = ev
df['release_speed'].iloc[0] = release_speed
df['fav_platoon_split_for_batter'].iloc[0] = fav_platoon_split_for_batter
df['game_elevation'].iloc[0] = game_elevation
df['pull_percent'].iloc[0] = pull_percent

st.dataframe(df)

# p =  model.predict(df)

# st.write(p[0])
