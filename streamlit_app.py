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

#Data preparations
with st.sidebar:
  st.header('Input features')
  #gender,age,hypertension,heart_disease,smoking_history,bmi,HbA1c_level,blood_glucose_level
  gender=st.selectbox('Gender',('Male','Female'))
  age=st.slider("Adjust your age ",0,100)
  hypertension=st.radio('Hypertension',(0,1))
  heart_disease=st.radio('Heart_Disease',(0,1))

  #'never': 0, 'No Info': 1, 'current': 2, 'former': 3, 'ever': 4, 'not current': 5
  smoking_history=st.selectbox('Smoking_History',('never','No Info','current','former','ever','not current'))
  bmi=st.slider("Adjust your BMI ",6,80)
  HbA1c_level=st.number_input('Enter your HbA1c blood level')
  blood_glucose_level=st.number_input('Enter your Blood Glucose level')

  #create a dataframe for input features

  data={'gender',gender,
        'age',age,
        'hypertension',hypertension,
        'heart_disease',heart_disease,
        'smoking_history',smoking_history,
        'bmi',bmi,
        'HbA1c_level',HbA1c_level,
        'blood_glucose_level',blood_glucose_level}
  input_df=pd.DataFrame(data,index=[0])
  input_features=pd.concat([input_df,X],axis=0)
  

input_features
  
  
  
