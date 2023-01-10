import pandas as pd
import streamlit as st
#import numpy as np

def upload_multyfile():
    uploaded_files = st.file_uploader('Tải bảng điểm tại đây', accept_multiple_files=True)
    data = []
    for uploaded_file in uploaded_files:
        bytes_data = pd.read_excel(uploaded_file, engine='openpyxl')
        data.append(bytes_data)
    return data

def upload_multyfile_sum():
    uploaded_files = st.file_uploader('Tải bảng điểm tổng hợp tại đây', accept_multiple_files=True)
    data = []
    for uploaded_file in uploaded_files:
        bytes_data = pd.read_csv(uploaded_file)
        data.append(bytes_data)
    return data

def load_data(uploaded_files):
    #uploaded_files = st.file_uploader('Tải bảng điểm tại đây', accept_multiple_files=True)
    data = []
    for uploaded_file in uploaded_files:
        bytes_data = pd.read_excel(uploaded_file, engine='openpyxl')
        data.append(bytes_data)
    data = pd.concat(data)
    return data