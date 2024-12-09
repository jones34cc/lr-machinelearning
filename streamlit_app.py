import streamlit as st
import pandas as pd

st.title('🐱‍🏍Diabetes Prediction App ')
st.info('This app builds a machine learning model')

with st.expander('Data'):
  st.write('Raw data**')
  df=pd.read_csv('https://raw.githubusercontent.com/jones34cc/diabetes-data/refs/heads/main/diabetes_prediction_dataset.csv')
  df
