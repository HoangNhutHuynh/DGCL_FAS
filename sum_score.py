import numpy as np
#import streamlit as st
def sum_score(data):
    test_rate = 0.25
    exercise_rate = 0.05
    essay_rate = 0.2
    exam_rate = 0.5
    
    data.loc[data['Kiểm tra - 25%']==13, ['Kiểm tra - 25%']] = 0
    data.loc[data['Bài tập - 5%']==13, ['Bài tập - 5%']] = 0
    data.loc[data['Bài tập lớn/Tiểu luận - 20%']==13, ['Bài tập lớn/Tiểu luận - 20%']] = 0
    
    
    data['Điểm tổng kết - 100%'] = np.abs(data['Kiểm tra - 25%']*test_rate + 
                                          data['Bài tập - 5%']*exercise_rate +
                                          data['Bài tập lớn/Tiểu luận - 20%']*essay_rate +
                                          data['Thi - 50%']*exam_rate)
    data.loc[data["Thi - 50%"] == 13, ["Thi - 50%", "Điểm tổng kết - 100%", 'Bài tập lớn/Tiểu luận - 20%', 'Kiểm tra - 25%', 'Bài tập - 5%']] = 0
    return data


def Muc_dat_thuc_te(value_above_7, value_above_8):
    if 0.0 <= value_above_7 < 0.1:
        score = 0
    elif 0.1 <= value_above_7 < 0.2:
        score = 0.5
    elif 0.2 <= value_above_7 < 0.3:
        score = 1.0
    elif 0.3 <= value_above_7 < 0.4:
        score = 1.5
    elif 0.4 <= value_above_7 < 0.5:
        score = 2.0
    elif 0.5 <= value_above_7 < 0.6:
        score = 2.5
    elif 0.6 <= value_above_7 < 0.7:
        score = 3.0
    elif 0.7 <= value_above_7 < 0.8:
        score = 3.5
    elif 0.7 <= value_above_8 < 0.8:
        score = 4.0
    elif 0.8 <= value_above_8 < 0.9:
        score = 4.5
    elif 0.9 <= value_above_8 < 1.0:
        score = 5.0
    return score

def MDTT(data):
    total_avb_7 = np.sum(data['TB theo CĐRMH'] >= 7.00) / data['TB theo CĐRMH'].count()
    total_avb_8 = np.sum(data['TB theo CĐRMH'] >= 8.00) / data['TB theo CĐRMH'].count()
    score = np.round(Muc_dat_thuc_te(total_avb_7, total_avb_8), 2)
    return score








    