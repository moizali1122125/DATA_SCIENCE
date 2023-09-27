import streamlit as st
import joblib
# Create a web form for user input
st.sidebar.header('Enter Diamond Characteristics')
carat = st.sidebar.slider('Carat', 0.2, 5.0, value=1.0,step=0.1 )
cut = st.sidebar.selectbox('Cut', ['Ideal', 'Premium', 'Very Good', 'Good', 'Fair'])
color = st.sidebar.selectbox('Color', ['D', 'E', 'F', 'G', 'H', 'I', 'J'])
clarity = st.sidebar.selectbox('Clarity', ['IF', 'VVS1', 'VVS2', 'VS1', 'VS2', 'SI1', 'SI2', 'I1'])
# load the model
model = joblib.load("19b_model.pkl")
# Make a prediction based on user input
prediction = model.predict([(carat, cut, color, clarity)])
# Display the prediction to the user
st.write['']
st.write['']
st.subheader('Predicted Diamond Price')
st.write(f'${prediction[0]:,.2f}')
