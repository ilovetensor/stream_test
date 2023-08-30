import streamlit as st
import pandas as pd


st.title('🎈 App Name')

st.write('Hello world!')


df = pd.read_csv("https://github.com/dec1costello/stream_test/blob/main/Vars.csv")

with st.sidebar:
    st.markdown('<h1 style="font-family: Consolas; font-size: 34px;">Select Your Inputs Here...</h1>', unsafe_allow_html=True)
    options = df["EV"].dropna().tolist()
    player = st.selectbox('Player', options)
    

    if user_input != default_position:
        # Filter based on user input
        position = user_input
    else:
        # Default behavior with 'Position' derived from 'Player' column
        position = default_position

    # If the user has selected a position, update the position of the selected player
    if user_input != default_position:
        df.loc[df['Player'] == player, 'Position'] = position

    # Filter the dataframe based on the position
    df = df.loc[df['Position'] == position].reset_index(drop=True)
    st.write(position+" Template")
    st.markdown('<h1 style="font-family: Consolas; font-size: 34px;">..And Let The Magic Happen ➡️</h1>', unsafe_allow_html=True)
