import streamlit as st
import pandas as pd


st.title('🎈 App Name')

st.write('Hello world!')


df = pd.read_csv("https://github.com/dec1costello/stream_test/blob/main/Vars.csv")

with st.sidebar(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
    # options = df["EV"].dropna().tolist()
    # player = st.selectbox('Player', options)
)
