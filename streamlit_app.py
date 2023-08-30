import streamlit as st

st.title('🎈 App Name')

st.write('Hello world!')

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)
