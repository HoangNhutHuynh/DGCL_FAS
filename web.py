import streamlit as st
#import pandas as pd
#import matplotlib.pyplot as plt
from histogramchart import histogram_bart
from sum_score import sum_score, MDTT
from KHDG import TS_DRMH
from PIL import Image
from download_data import convert_df
from Upload_file import upload_multyfile, upload_multyfile_sum, load_data
from make_df import make_df, make_df_sum
import numpy as np
from make_pdf import make_pdf
#import streamlit_authenticator as stauth

primaryColor="#6eb52f"
backgroundColor="#f0f0f5"
secondaryBackgroundColor="#e0e0ef"
textColor="#262730"
font="sans serif"
logo = Image.open('C:/DATA/CDR/61b17a711281b213efc3e79d.png')
st.image(logo)
st.markdown("<h1 style='text-align: center; color: black;'>ĐÁNH GIÁ MỨC ĐỘ TÍCH LŨY CHUẨN ĐẦU RA MÔN HỌC</h1>", unsafe_allow_html = True)
#tab1, tab2 = st.tabs(["Giảng viên", "Quản trị viên"])
#with tab1:
st.markdown("<h1 style='text-align: center; color: black;'>Tải bảng điểm</h1>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["🗃 Data", "📈 Chart"])

with tab1:
    uploaded_files = st.file_uploader('Tải bảng điểm tại đây', accept_multiple_files=True)
    option_subject = st.selectbox('Chọn môn học', ('PH1007', 'MT1005', 'PH1005', 'MT1007', 'AS1001', 'MT1003'))
    row1_space1, row1_1, row1_space2, row1_2, row1_space3 = st.columns((0.01, 1.4, 0.1, 1, 0.01))
    if uploaded_files:
        df1 = load_data(uploaded_files)
        
        kt_13 = np.sum(df1['Kiểm tra - 25%'] > 10.0)
        bt_13 = np.sum(df1['Bài tập - 5%'] > 10.0)
        btl_13 = np.sum(df1['Bài tập lớn/Tiểu luận - 20%'] > 10.0)
        thi_13 = np.sum(df1['Thi - 50%'] > 10.0)
        sum_score(df1)
        with row1_1:
            st.dataframe(df1)
        with row1_2:
            #st.text("Tổng số sinh viên trong mẫu: " + str(df1['Tên'].count())+ ' sinh viên')
            st.text("Tổng số sinh viên vắng kiểm tra: " + str(kt_13)+ ' sinh viên')
            st.text("Tổng số sinh viên vắng bài tập lớn: " + str(btl_13)+ ' sinh viên')
            st.text("Tổng số sinh viên vắng bài tập: " + str(bt_13)+ ' sinh viên')
            st.text("Tổng số sinh viên vắng thi: " + str(thi_13)+ ' sinh viên')
            st.text("Tổng số sinh viên tính toán: " + str(df1['Mã sinh viên'].count())+ ' sinh viên')
            
        with tab2:
            st.title("Options")
            option = st.selectbox('Đồ thị các cột điểm',('Kiểm tra', 'Bài tập', 'Bài tập lớn/Tiểu luận', 'Thi', "Điểm tổng kết"))
            st.write('Cột điểm:', option)
            if option == "Kiểm tra":
                histogram_bart(df1['Kiểm tra - 25%'])
            if option == "Bài tập":
                histogram_bart(df1['Bài tập - 5%'])
            if option == 'Bài tập lớn/Tiểu luận':
                histogram_bart(df1['Bài tập lớn/Tiểu luận - 20%'])
            if option == 'Thi':
                histogram_bart(df1['Thi - 50%'])
            if option == "Điểm tổng kết":
                histogram_bart(df1['Điểm tổng kết - 100%'])            
            #st.set_option('deprecation.showPyplotGlobalUse', False)      
    if option_subject:
        check = st.checkbox('Xác nhận môn đã chọn')
        if st.button('Tính trọng số của CĐRMH'):
            st.header('Bảng thống kê chuẩn đầu ra môn học', )
            row4_space1, row_rs, row4_s = st.columns((0.01, 1, 0.1))
            with row_rs:
                if option_subject == 'PH1007':
                    df1 = TS_DRMH(df1, 'Define_para.xlsx', 'PH1007')
                    st.dataframe(df1)
                    csv = convert_df(df1)
                    st.write('***Tệp tải về ở định dạng .csv nên không thể chỉnh sửa***')
                    st.download_button("Tải bảng điểm", csv, "bang_diem_{}.csv".format('PH1007'), "text/csv", key='download-file.csv')
                    make_pdf(option_subject, kt_13, bt_13, btl_13, thi_13)
                if option_subject == 'PH1005':
                    df1 = TS_DRMH(df1, 'Define_para.xlsx', 'PH1005')
                    st.dataframe(df1)
                    csv = convert_df(df1)
                    st.write('***Tệp tải về ở định dạng .csv nên không thể chỉnh sửa***')
                    st.download_button("Tải bảng điểm", csv, "bang_diem_{}.csv".format('PH1005'), "text/csv", key='download-file.csv')
                if option_subject == 'MT1005':
                    df1 = TS_DRMH(df1, 'Define_para.xlsx', 'MT1005')
                    st.dataframe(df1)
                    csv = convert_df(df1)
                    st.write('***Tệp tải về ở định dạng .csv nên không thể chỉnh sửa***')
                    st.download_button("Tải bảng điểm", csv, "bang_diem_{}.csv".format('MT1005'), "text/csv", key='download-file.csv')
                if option_subject == 'MT1007':
                    df1 = TS_DRMH(df1, 'Define_para.xlsx', 'MT1007')
                    st.dataframe(df1)
                    csv = convert_df(df1)
                    st.write('***Tệp tải về ở định dạng .csv nên không thể chỉnh sửa***')
                    st.download_button("Tải bảng điểm", csv, "bang_diem_{}.csv".format('MT1007'), "text/csv", key='download-file.csv')
                if option_subject == 'AS1001':
                    df1 = TS_DRMH(df1, 'Define_para.xlsx', 'AS1001')
                    st.dataframe(df1)
                    csv = convert_df(df1)
                    st.write('***Tệp tải về ở định dạng .csv nên không thể chỉnh sửa***')
                    st.download_button("Tải bảng điểm", csv, "bang_diem_{}.csv".format('AS1001'), "text/csv", key='download-file.csv') 
                if option_subject == 'MT1003':
                    df1 = TS_DRMH(df1, 'Define_para.xlsx', 'MT1003')
                    st.dataframe(df1)
                    csv = convert_df(df1)
                    st.write('***Tệp tải về ở định dạng .csv nên không thể chỉnh sửa***')
                    st.download_button("Tải bảng điểm", csv, "bang_diem_{}.csv".format('MT1003'), "text/csv", key='download-file.csv')
                
           
