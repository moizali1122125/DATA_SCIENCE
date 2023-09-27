from random import Random
import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
df = sns.load_dataset('titanic')
df = df.dropna()
# make containers
header = st.container()
data_sets = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title('Titanic App')

with data_sets:
    st.header('Titanic crash')
    st.write(df.head(10))

    st.subheader('Sex chart')
    st.bar_chart(df['sex'].value_counts())
    st.subheader('Class chart')
    st.bar_chart(df['class'].value_counts())

with features:
    st.header('These are the features of Titanic')
    st.markdown('1. **Feature 1:** >>>>>>>>>')
    st.markdown('2. **Feature 2:** <<<<<<<<<')
with model_training:
    st.header('Data of patients')
    # making coulumns
    input, display = st.columns(2)
    max_depth=input.slider('How many people do you know?', min_value=10,max_value=100,value=20,step=5)

# Random Forrest (RF)
n_estimators = input.selectbox('How many tree should be there in a RF', options=[50,100,200,300,'No Limit']) 

# adding list of features
st.subheader('List of Columns')
input.write(df.columns)

# input from user
input_features = input.text_input('Which feature we should use?')

# Machine learning model
# Make condition:
if n_estimators =='No limit':
    model = RandomForestRegressor(max_depth=max_depth)
else:
   random_r = RandomForestRegressor(max_depth=max_depth,n_estimators=n_estimators)

model = RandomForestRegressor(max_depth=max_depth,n_estimators=n_estimators)
X = df[[input_features]]
y = df[['fare']]
model.fit(X,y)
pred = model.predict(y)

# Display metrices
display.subheader('Mean absolute error of the model is: ')
display.write(mean_absolute_error(y,pred))
display.subheader('Mean squared error of model is: ')
display.write(mean_squared_error(y,pred))
display.subheader('r_2 score of model is: ')
display.write(r2_score(y,pred))