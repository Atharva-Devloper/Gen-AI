import streamlit as st
import pandas as pd

st.title("Hello Streamlit!")

name = st.text_input("Enter your name:")

age = st.slider("Select your age:", 0, 100, 25)

st.write(f"Your age is {age}.")

if name:
    st.write(f"Hello, {name}!")
    
options = ["Option 1", "Option 2", "Option 3"]    
choice = st.selectbox("Choose an option:", options)
st.write(f"You selected: {choice}")

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],    
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV File:  ", type="csv")

if uploaded_file is not None:
    df= pd.read_csv(uploaded_file)
    st.write(df)