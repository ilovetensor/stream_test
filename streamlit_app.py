import streamlit as st
from utils import PrepProcesor, columns 

import numpy as np
import pandas as pd
import joblib

model = joblib.load('xgbpipe.joblib')

st.title('Distance Predictor')

la = st.slider("Choose LA",-50,50)

ev = st.slider("Choose EV",0,100)

release_speed = st.slider("Choose Release Speed",60,110)

fav_platoon_split_for_batter = st.selectbox("Good Platoon Split?", [0,1])

game_elevation = st.slider("Choose Game Elevation",20,7349) 

pull_percent =  st.slider("Choose Pull %",0,100)

prediction = 0

# def predict(): 
#     row = np.array([la,ev,release_speed,fav_platoon_split_for_batter,game_elevation,pull_percent]) 
#     X = pd.DataFrame([row], columns = columns)
#     prediction = model.predict(X)
#     if prediction[0] == 1: 
#         st.success('Passenger Survived :thumbsup:')
#     else: 
#         st.error('Passenger did not Survive :thumbsdown:') 

# trigger = st.button('Predict', on_click=predict)

st.title(prediction)

