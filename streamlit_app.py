import streamlit as st
import pandas as pd


st.title('🎈 App Name')

st.write('Hello world!')


df = pd.read_csv("https://github.com/dec1costello/stream_test/blob/main/Vars.csv")

with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )


# options = df["EV"].dropna().tolist()
# player = st.selectbox('Player', options)
