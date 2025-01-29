import streamlit as st
import numpy as np
import pandas as pd

##Title of my application

st.title('Hello and welcome to my first Streamlit application')

##Display a simple text
st.write('How are you doing today?')

##Create a simple dataframe
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

##Display the dataframe
st.write('Here is a simple dataframe')
st.write(df)

##Create a line chart

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
    )
st.line_chart(chart_data)


