import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier


st.title("ML App with Streamlit")

@st.cache_data # This function will be cached, meaning that it 
          #will only be run once and the results will be stored in memory for subsequent runs
def load_data():
    iris_data = load_iris()
    df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
    df['species'] = iris_data.target
    return df, iris_data.target_names

df, target_names = load_data()

model = RandomForestClassifier()
model.fit(df.iloc[:,:-1], df['species'])

st.sidebar.title("Input Features")

sepal_length = st.sidebar.slider("Feature 1", float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()))
sepal_width = st.sidebar.slider("Feature 2", float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()))
petal_length = st.sidebar.slider("Feature 3", float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()))
petal_width = st.sidebar.slider("Feature 4", float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()))
                                
input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

prediction = model.predict(input_data)
predicted_species = target_names[prediction][0]

st.write(f"The predicted species is {predicted_species}")