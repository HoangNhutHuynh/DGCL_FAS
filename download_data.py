import streamlit as st
#import pandas as pd
#df = pd.read_csv("dir/file.csv")
@st.cache
def convert_df(df):
   return df.to_csv().encode('utf-8-sig')
   
   