import streamlit as st
import pandas as pd

st.title("Streamlit text input example")
st.write("Please enter your name in the text box below")
name = st.text_input("Name")
age= st.slider("Select your age:", 1, 100, 25)

if name :
    st.write(f"Hello {name}")

st.write(f"Your age is {age}")

##Write a select box

st.write("Please select your favorite color")
colours = ["Red", "Blue", "Green", "Yellow", "Orange"]
color = st.selectbox("Color", colours)
if color:
    st.write(f"Your favorite color is {color}")


data = {
     "Name" : ["John", "Anna", "Peter", "Linda"],
     "Age" : [25, 26, 27, 28],
     "City" : ["New York", "Paris", "Berlin", "London"]

}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv", index=False)

st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)

