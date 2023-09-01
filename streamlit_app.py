import streamlit as st
import pandas as pd
#import joblib
import pickle

#joblib now imports but wtf no model........
#joblib_model = joblib.load('xgbr.joblib')

st.title('Distance Predictor')

la = st.slider("Launch Angle",0,50, value=25)
ev = st.slider("Exit Velocity",0,120, value=60)
pull_percent =  st.slider("Pull %",0.0,1.0, value = 0.5)
#honestly take pitch speed out... 
release_speed = st.slider("Pitch Speed",60,110, value=85)
game_elevation = st.slider("Elevation",20,7349, value=3665) 
fav_platoon_split_for_batter = st.slider("Favorable Platoon", 0,1, value = 1)


df = pd.read_csv('final_input.csv')

df['launch_angle'].iloc[0] = la
df['launch_speed'].iloc[0] = ev
df['release_speed'].iloc[0] = release_speed
df['fav_platoon_split_for_batter'].iloc[0] = fav_platoon_split_for_batter
df['game_elevation'].iloc[0] = game_elevation
df['pull_percent'].iloc[0] = pull_percent

df_display = df

#display for debugging purposes
st.dataframe(df_display)


#pickled_model = pickle.load(open('model.pkl', 'rb'))
# pred = pickled_model.predict(final_vars)

#p =  joblib_model.predict(df)

co_0, co_1, co_2, co_3, co_4, co_5, co_6 = st.columns(7)

with co_3:
    ok = st.button("Predict Distance")

# st.write(p[0])
