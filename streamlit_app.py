import streamlit as st
import pandas as pd


st.title('🎈 App Name')

st.write('Hello world!')


df = pd.read_csv("https://github.com/dec1costello/stream_test/blob/main/Vars.csv")

with st.sidebar:
    st.markdown('<h1 style="font-family: Consolas; font-size: 34px;">Select Your Inputs Here...</h1>', unsafe_allow_html=True)
    options = df["EV"].dropna().tolist()
    player = st.selectbox('Player', options)
