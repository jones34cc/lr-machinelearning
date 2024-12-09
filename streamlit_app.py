import streamlit as st
import pandas as pd

st.title('🐱‍🏍Diabetes Prediction App ')
st.info('This app builds a machine learning model')

with st.expander('Data'):
  st.write('**Raw data**')
  df=pd.read_csv('https://raw.githubusercontent.com/jones34cc/diabetes-data/refs/heads/main/diabetes_prediction_dataset.csv')
  df

st.write('**X**')
X=df.drop('diabetes',axis=1)
X

st.write('**Y**')
Y=df.diabetes
Y


with st.expander('Data Visualization'):
  st.scatter_chart(data=df,x='bmi',y='blood_glucose_level',color='diabetes')
