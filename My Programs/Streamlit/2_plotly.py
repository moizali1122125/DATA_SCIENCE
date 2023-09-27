import pandas as pd
import streamlit as st
import plotly.express as px

st.title('Make app with combination of streamlit and plotly')

df = px.data.gapminder()
st.write(df)
st.write(df.columns)
st.write(df.describe())

# Data managment
year_option = df['year'].unique().tolist()
year = st.selectbox('Which year should we plot?',year_option,0)
# df = df[df['year']==year]

# Plotly
fig = px.scatter(df, x='gdpPercap',y='lifeExp', size='pop', color='country',hover_name='country',log_x=True,size_max=55,range_x=[100,100000],range_y=[20,90],
                animation_frame='year',animation_group='country') # add this for animation or Remove (df = df[df['year']==year])

fig.update_layout(width=800,height=400)
st.write(fig)
