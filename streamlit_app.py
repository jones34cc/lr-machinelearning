import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

st.title('🙆‍♀️Diabetes Prediction App ')
st.info('This app builds a machine learning model that predicts Diabetes percentage taking few parameters!!Enjoy')

with st.expander('Data'):
  st.write('**Raw data**')
  df=pd.read_csv('https://raw.githubusercontent.com/jones34cc/diabetes-data/refs/heads/main/diabetes_prediction_dataset.csv')
  df

  st.write('**X**')
  X_raw=df.drop('diabetes',axis=1)
  X_raw

  st.write('**Y**')
  Y=df.diabetes
  Y


with st.expander('Data Visualization'):
  st.scatter_chart(data=df,x='bmi',y='blood_glucose_level',color='diabetes')

#Input features
with st.sidebar:
  st.header('Input features')
  #gender,age,hypertension,heart_disease,smoking_history,bmi,HbA1c_level,blood_glucose_level
  gender=st.selectbox('Gender',('Male','Female'))
  age=st.slider("Adjust your age ",0,100)
  hypertension=st.radio('Hypertension',('No','Yes'))
  hypertension = 1 if hypertension == 'Yes' else 0
  heart_disease=st.radio('Heart_Disease',('No','Yes'))
  heart_disease = 1 if heart_disease == 'Yes' else 0

  #'never': 0, 'No Info': 1, 'current': 2, 'former': 3, 'ever': 4, 'not current': 5
  smoking_history=st.selectbox('Smoking_History',('never','No Info','current','former','ever','not current'))
  bmi=st.slider("Adjust your BMI ",6,80)
  HbA1c_level=st.number_input('Enter your HbA1c blood level')
  blood_glucose_level=st.number_input('Enter your Blood Glucose level')

  #create a dataframe for input features

  data={'gender':gender,
        'age':age,
        'hypertension':hypertension,
        'heart_disease':heart_disease,
        'smoking_history':smoking_history,
        'bmi':bmi,
        'HbA1c_level':HbA1c_level,
        'blood_glucose_level':blood_glucose_level}
  input_df=pd.DataFrame(data,index=[0])
  input_features=pd.concat([input_df,X_raw],axis=0)

with st.expander('Input Features'):
  st.write('**Recent Data**')
  input_df
  st.write('**Combined Data**')
  input_features


  #Data preparation
  #encode x
  encode=['gender','smoking_history']
  df_features=pd.get_dummies(input_features,prefix=encode)
  X=df_features[1:]
  input_row=df_features[:1]

  
  


with st.expander('Data preparation'):
  st.write('**Encoded X (input features)**')
  input_row
  st.write('**Encoded Y**')
  Y


#Model Training and inference
##Train the ml model
clf=RandomForestClassifier()
clf.fit(X,Y)

##Apply model to make predictions
prediction=clf.predict(input_row)
prediction_proba=clf.predict_proba(input_row)

df_prediction_proba=pd.DataFrame(prediction_proba)
df_prediction_proba.columns=['No Diabetes !! Congratulations🎉🎉','Diabetes😱😱Better Luck Next Time :(']
df_prediction_proba.rename(columns={0:'No Diabetes !! Congratulations🎉🎉',
                                 1:'Diabetes😱😱Better Luck Next Time :('})


#Display Predicted results
st.subheader('Diabetes Prediction')
st.dataframe(df_prediction_proba,
             column_config={
               'No Diabetes !! Congratulations🎉🎉':st.column_config.ProgressColumn(
                 'No Diabetes !! Congratulations🎉🎉',
                 format='%f',
                 width='medium',
                 min_value=0,
                 max_value=1
                 ),
                 'Diabetes😱😱Better Luck Next Time :(':st.column_config.ProgressColumn(
                 'Diabetes😱😱Better Luck Next Time :(',
                 format='%f',
                 width='medium',
                 min_value=0,
                 max_value=1
                 ),
                 },hide_index=True)
                 

diabetes_features=np.array(['No Diabetes !! Congratulations🎉🎉','Diabetes😱😱Better Luck Next Time :('])
st.success(str(diabetes_features[prediction][0]))


  
  
  
