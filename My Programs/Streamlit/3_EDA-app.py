import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

st.markdown('''# **Exploratory Data Analysis**''')

# Upload file from pc
with st.sidebar.header('Upload your dataset (.csv)'):
    uploaded_file = st.sidebar.file_uploader('Upload your file', type=['csv'])  #Button
    df = sns.load_dataset('titanic')
    st.sidebar.markdown('[Example CSV file](df)')

# Profiling report for pandas
if uploaded_file is not None:
    @st.cache # for when i upload data he saved and cannot load every time (increase speed of app)
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input Data**')
    st.write(df)
    st.write('---')
    st.header('**Profiling report with pandas**')
    st_profile_report(pr)
else:
    st.info('Awaiting for DATA File')
    if st.button('Press to use Example DATA'):
        @st.cache
        def load_data():
            a = pd.DataFrame(np.random.rand(100,5),
                             columns=['age','banana','cat','dog','ear'])
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input Data**')
        st.write(df)
        st.write('---')
        st.header('**Profiling report with pandas**')
        st_profile_report(pr)
