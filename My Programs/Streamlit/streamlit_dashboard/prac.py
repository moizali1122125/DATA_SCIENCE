# Import Libraries
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Import Data
df = pd.read_csv('diabetes.csv')

# Write heading Names
st.header('Diabetes Prediction App')
st.sidebar.header('Patient Data')
# Show the Description of Data
st.subheader('Description Stats of Data')
st.write(df.describe())

# Select Data on X and y axis
X=df.drop(['Outcome'],axis=1)
y=df.iloc[:,-1]
# Use train_test_split for checking Accuracy Score
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)

# Create Function
def user_report():
          pregnancies = st.sidebar.slider('Pregnancies',0,17,2)
          glucose     = st.sidebar.slider('Glucose',0,199,110)
          bp          = st.sidebar.slider('BloodPressure',0,122,80)
          sk          = st.sidebar.slider('SkinThickness',0,99,12)
          insulin     = st.sidebar.slider('Insulin',0,846,80)
          bmi         = st.sidebar.slider('BMI',0,67,5)
          dpf         = st.sidebar.slider('DiabetesPedigreeFunction',0.07,2.42,0.37)
          age         = st.sidebar.slider('Age',21,81,33)
          # Define Dictionary
          user_report_data = {
              'pregnancies': pregnancies,
              'glucose'    : glucose,
              'bp'         : bp,
              'sk'         : sk,
              'insulin'    : insulin,
              'bmi'        : bmi,
              'dpf'        : dpf,
              'age'        : age        }
          # Showing Function Data
          report_data = pd.DataFrame(user_report_data, index=[0])
          return report_data
     
# Sliders Heading
user_data = user_report()
st.subheader('Patient Data')
st.write('user_data')

# Creating Machine Learning Model
rc = RandomForestClassifier()
rc.fit(X_train,y_train)
user_result = rc.predict(user_data)

# Visualization
st.title('Visualized Patient Data')
# Color Function
if user_result[0] == 0:
     color = 'blue'
else:
     color = 'red'

# Age vs Pregnancies 
st.header('Pregnancy Count Graph (Others vs Yours)')
fig_preg = plt.figure()
ax1 = sns.scatterplot(x='Age', y='Pregnancies', data=df, hue='Outcome', palette='Greens')
ax2 = sns.scatterplot(x= user_data['age'], y=user_data['pregnancies'], s=150, color=color)
plt.xticks(np.arange(10,100,5))
plt.yticks(np.arange(0,20,2))
plt.title ('0 - Healthy  &  1 - Diabetic')
st.pyplot(fig_preg)

st.header("Your Report: ")
output = ''
if user_result[0]==0:
     output = "You are Healthy 😍"
     st.balloons()
else:
    output= "You are not Healthy"
    st.warning("Sugar, Sugar, Sugar")
st.title(output)
# st.subheader('Accuracy:')
# st.write(str(accuracy_score(y_test,rc.predict(X_test))*100 + '%'))