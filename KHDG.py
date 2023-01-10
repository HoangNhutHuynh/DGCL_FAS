import numpy as np
#import streamlit as st
import pandas as pd
from sum_score import MDTT, Muc_dat_thuc_te

def rate(data, CDR):
    #value_above_7 = np.sum(data[CDR] >= 7.00)
    value_above_8 = np.sum(data[CDR] >= 8.00)
    #rate_above_7 = np.round(value_above_7/data[CDR].count(), 2)
    rate_above_8 = np.round(value_above_8/data[CDR].count(), 2)
    #data["Tỉ lệ đạt trên mức điểm 7 theo {}".format(CDR)] = ''
    #data["Tỉ lệ đạt trên mức điểm 7 theo {}".format(CDR)][0] = str(rate_above_7)
    #data["Tỉ lệ đạt trên mức điểm 8 theo {}".format(CDR)] = ''
    #data["Tỉ lệ đạt trên mức điểm 8 theo {}".format(CDR)][0] = rate_above_8 
    return rate_above_8

def TS_DRMH(data, df_para, subject):
    data_para = pd.read_excel(df_para, sheet_name= subject)
    
    kynd = data_para['Kỳ vọng ngưỡng đạt'][0]
    
    tl_01 = data_para['Thảo luận/Thực hành tại lớp'][1]
    tl_02 = data_para['Thảo luận/Thực hành tại lớp'][2]
    tl_03 = data_para['Thảo luận/Thực hành tại lớp'][3]
    tl_04 = data_para['Thảo luận/Thực hành tại lớp'][4]
    tl_05 = data_para['Thảo luận/Thực hành tại lớp'][5]
    tl_06 = data_para['Thảo luận/Thực hành tại lớp'][6]
    tl_07 = data_para['Thảo luận/Thực hành tại lớp'][7]
    
    btl_01 = data_para['Bài tập lớn'][1]
    btl_02 = data_para['Bài tập lớn'][2]
    btl_03 = data_para['Bài tập lớn'][3]
    btl_04 = data_para['Bài tập lớn'][4]
    btl_05 = data_para['Bài tập lớn'][5]
    btl_06 = data_para['Bài tập lớn'][6]
    btl_07 = data_para['Bài tập lớn'][7]
    
    gk_01 = data_para['Thi giữa kỳ'][1]
    gk_02 = data_para['Thi giữa kỳ'][2]
    gk_03 = data_para['Thi giữa kỳ'][3]
    gk_04 = data_para['Thi giữa kỳ'][4]
    gk_05 = data_para['Thi giữa kỳ'][5]
    gk_06 = data_para['Thi giữa kỳ'][6]
    gk_07 = data_para['Thi giữa kỳ'][7]
    
    ck_01 = data_para['Thi cuối kỳ'][1]
    ck_02 = data_para['Thi cuối kỳ'][2]
    ck_03 = data_para['Thi cuối kỳ'][3]
    ck_04 = data_para['Thi cuối kỳ'][4]
    ck_05 = data_para['Thi cuối kỳ'][5]
    ck_06 = data_para['Thi cuối kỳ'][6]
    ck_07 = data_para['Thi cuối kỳ'][7]  
    
    
    data['TB theo L.O.1'] = np.round(np.abs(data['Kiểm tra - 25%']*gk_01 + 
                                          data['Bài tập - 5%']*tl_01 +
                                          data['Bài tập lớn/Tiểu luận - 20%']*btl_01 +
                                          data['Thi - 50%']*ck_01) / data_para['Trọng số theo CĐRMH'][1],1)
    
    data['TB theo L.O.2'] = np.round(np.abs(data['Kiểm tra - 25%']*gk_02 + 
                                          data['Bài tập - 5%']*tl_02 +
                                          data['Bài tập lớn/Tiểu luận - 20%']*btl_02 +
                                          data['Thi - 50%']*ck_02) / data_para['Trọng số theo CĐRMH'][2], 1)
    
    data['TB theo L.O.3'] = np.round(np.abs(data['Kiểm tra - 25%']*gk_03 + 
                                          data['Bài tập - 5%']*tl_03 +
                                          data['Bài tập lớn/Tiểu luận - 20%']*btl_03 +
                                          data['Thi - 50%']*ck_03) / data_para['Trọng số theo CĐRMH'][3], 1)

    data['TB theo L.O.4'] = np.round(np.abs(data['Kiểm tra - 25%']*gk_04 + 
                                          data['Bài tập - 5%']*tl_04 +
                                          data['Bài tập lớn/Tiểu luận - 20%']*btl_04 +
                                          data['Thi - 50%']*ck_04) / data_para['Trọng số theo CĐRMH'][4], 1)
    
    data['TB theo L.O.5'] = np.round(np.abs(data['Kiểm tra - 25%']*gk_05 + 
                                          data['Bài tập - 5%']*tl_05 +
                                          data['Bài tập lớn/Tiểu luận - 20%']*btl_05 +
                                          data['Thi - 50%']*ck_05) / data_para['Trọng số theo CĐRMH'][5], 1)
    
    data['TB theo L.O.6'] = np.round(np.abs(data['Kiểm tra - 25%']*gk_06 + 
                                          data['Bài tập - 5%']*tl_06 +
                                          data['Bài tập lớn/Tiểu luận - 20%']*btl_06 +
                                          data['Thi - 50%']*ck_06) / data_para['Trọng số theo CĐRMH'][6], 1)
    
    data['TB theo L.O.7'] = np.round(np.abs(data['Kiểm tra - 25%']*gk_07 + 
                                          data['Bài tập - 5%']*tl_07 +
                                          data['Bài tập lớn/Tiểu luận - 20%']*btl_07 +
                                          data['Thi - 50%']*ck_07) / data_para['Trọng số theo CĐRMH'][7], 1)
    data.fillna(0, inplace= True)
    
    data['TB theo CĐRMH'] = (data['TB theo L.O.1'] * data_para['Trọng số trung bình CĐRMH'][1]
                            + data['TB theo L.O.2'] * data_para['Trọng số trung bình CĐRMH'][2]
                            + data['TB theo L.O.3'] * data_para['Trọng số trung bình CĐRMH'][3]
                            + data['TB theo L.O.4'] * data_para['Trọng số trung bình CĐRMH'][4] 
                            + data['TB theo L.O.5'] * data_para['Trọng số trung bình CĐRMH'][5] 
                            + data['TB theo L.O.6'] * data_para['Trọng số trung bình CĐRMH'][6]
                            + data['TB theo L.O.7'] * data_para['Trọng số trung bình CĐRMH'][7]) / (data_para['Trọng số trung bình CĐRMH'][0])
    
    value_above_7 = np.sum(data['TB theo CĐRMH'] >= 7.00)
    value_above_8 = np.sum(data['TB theo CĐRMH'] >= 8.00)
    rate_above_7 = np.round(value_above_7/data['TB theo CĐRMH'].count(), 2)
    rate_above_8= np.round(value_above_8/data['TB theo CĐRMH'].count(), 2)
    
    data['    '] = ''
    data["Tỉ lệ trung bình"] = ''
    data["Tỉ lệ trung bình"][0] = 'TB theo L.O.1'
    data["Tỉ lệ trung bình"][1] = 'TB theo L.O.2'
    data["Tỉ lệ trung bình"][2] = 'TB theo L.O.3'
    data["Tỉ lệ trung bình"][3] = 'TB theo L.O.4'
    data["Tỉ lệ trung bình"][4] = 'TB theo L.O.5'
    data["Tỉ lệ trung bình"][5] = 'TB theo L.O.6'
    data["Tỉ lệ trung bình"][6] = 'TB theo L.O.7'
    data['Tỉ lệ trung bình'][7] = 'Chuẩn đầu ra môn học'
    
    data['Kỳ vọng ngưỡng đạt'] = ''
    data['Kỳ vọng ngưỡng đạt'][0] = kynd    
    data['Kỳ vọng ngưỡng đạt'][1] = kynd
    data['Kỳ vọng ngưỡng đạt'][2] = kynd
    data['Kỳ vọng ngưỡng đạt'][3] = kynd
    data['Kỳ vọng ngưỡng đạt'][4] = kynd
    data['Kỳ vọng ngưỡng đạt'][5] = kynd
    data['Kỳ vọng ngưỡng đạt'][6] = kynd
    data['Kỳ vọng ngưỡng đạt'][7] = kynd
    
    data['Tỷ lệ đạt thực tế'] = ''
    data['Tỷ lệ đạt thực tế'][0] = rate(data, 'TB theo L.O.1')
    data['Tỷ lệ đạt thực tế'][1] = rate(data, 'TB theo L.O.2')
    data['Tỷ lệ đạt thực tế'][2] = rate(data, 'TB theo L.O.3')
    data['Tỷ lệ đạt thực tế'][3] = rate(data, 'TB theo L.O.4')
    data['Tỷ lệ đạt thực tế'][4] = rate(data, 'TB theo L.O.5')
    data['Tỷ lệ đạt thực tế'][5] = rate(data, 'TB theo L.O.6')
    data['Tỷ lệ đạt thực tế'][6] = rate(data, 'TB theo L.O.7')
    data['Tỷ lệ đạt thực tế'][7] = np.round(np.sum(data['Điểm tổng kết - 100%'] >= 8.00)/data['Mã sinh viên'].count(), 2)
    
    data['     '] = ''
    data['Chuẩn đầu ra đánh giá'] = ''
    data['Chuẩn đầu ra đánh giá'][0] = data_para['CĐR được đánh giá'][0]
    data['Ngưỡng kỳ vọng'] = ''
    data['Ngưỡng kỳ vọng'][0] = data_para['Ngưỡng kỳ vọng'][0]
    data['Kết quả đánh giá thực tế'] = ''
    
    score = MDTT(data=data)
    score_tt = data['Ngưỡng kỳ vọng'][0]
    data['Kết quả đánh giá thực tế'][0] = score

    return data

