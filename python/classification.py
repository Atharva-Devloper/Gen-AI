import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    df['species'] = iris.target
    return df, iris.target_names

df, target_names = load_data()

model = RandomForestClassifier()
model.fit(df.iloc[:, :-1], df['species'])

st.sidebar.title("Iris Species Prediction")
sepal_length = st.sidebar.slider("Sepal Length (cm)", float(df['sepal_length'].min()), float(df['sepal_length'].max()), float(df['sepal_length'].mean()))
sepal_width = st.sidebar.slider("Sepal Width (cm)", float(df['sepal_width'].min()), float(df['sepal_width'].max()), float(df['sepal_width'].mean()))
petal_length = st.sidebar.slider("Petal Length (cm)", float(df['petal_length'].min()), float(df['petal_length'].max()), float(df['petal_length'].mean()))
petal_width = st.sidebar.slider("Petal Width (cm)", float(df['petal_width'].min()), float(df['petal_width'].max()), float(df['petal_width'].mean()))

input_data = pd.DataFrame(
    [[sepal_length, sepal_width, petal_length, petal_width]],
    columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
)

prediction = model.predict(input_data)
predicted_species = target_names[prediction[0]]

st.write("## Prediction")
st.write(f"Predicted Iris Species: {predicted_species}")
