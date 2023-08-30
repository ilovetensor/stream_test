import streamlit as st
import pandas as pd


st.title(':Baseball:')

df = pd.read_csv("Vars.csv")

la = st.sidebar.selectbox(
    "Launch Angle",
    (df['LA'])
)

ev = st.sidebar.selectbox(
    "Exit Velocity",
    (df['EV'])
)

st.write('Launch Angle:', la)

st.write('Exit Velocity:', ev)

# with st.sidebar:
#     add_radio = st.radio(
#         "Choose a shipping method",
#         ("Standard (5-15 days)", "Express (2-5 days)")
#     )


# options = df["EV"].dropna().tolist()
# player = st.selectbox('Player', options)
