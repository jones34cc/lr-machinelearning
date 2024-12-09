import streamlit as st
import pandas as pd

st.title('🐱‍🏍Diabetes Prediction App ')
st.info('This app builds a machine learning model')

df=pd.read_csv('https://raw.githubusercontent.com/jones34cc/diabetes-data/refs/heads/main/diabetes_prediction_dataset.csv')
df
