import streamlit as st
import pandas as pd


st.title('Baseball')

df = pd.read_csv("Vars.csv")


# Replicate Credentials
with st.sidebar:
    st.title('Enter La and EV here...')

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




passengerid = st.text_input("Input Passenger ID", '123456') 
pclass = st.selectbox("Choose class", [1,2,3])
name  = st.text_input("Input Passenger Name", 'John Smith')
sex = st.select_slider("Choose sex", ['male','female'])
age = st.slider("Choose age",0,100)
sibsp = st.slider("Choose siblings",0,10)
parch = st.slider("Choose parch",0,2)
ticket = st.text_input("Input Ticket Number", "12345") 
fare = st.number_input("Input Fare Price", 0,1000)
cabin = st.text_input("Input Cabin", "C52") 
embarked = st.select_slider("Did they Embark?", ['S','C','Q'])

# with st.sidebar:
#     add_radio = st.radio(
#         "Choose a shipping method",
#         ("Standard (5-15 days)", "Express (2-5 days)")
#     )


# options = df["EV"].dropna().tolist()
# player = st.selectbox('Player', options)
