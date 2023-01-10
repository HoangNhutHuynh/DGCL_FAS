import pandas as pd
from download_data import convert_df
import streamlit as st
import numpy as np

def make_df(score, subject):
    semeter = 'HKI'
    data = pd.read_excel('Define_para.xlsx', sheet_name=subject)
    tc = data['Tín chỉ'][0]
    nkv = data['Ngưỡng kỳ vọng'][0]
    d = {"Học kỳ": semeter, 
         "Môn học đánh giá": str(subject),
         "Tín chỉ": tc,
         "CĐR được đánh giá": data['CĐR được đánh giá'][0],
         'PIs được đánh giá': '',
         "Mức đạt kỳ vọng": nkv,
         "Mức đạt thực tế" : score,
         "Hành động (nếu có)":''}
    df = pd.DataFrame(data = [d], index=[1])
    df['Chênh lệch'] = np.abs(df['Mức đạt kỳ vọng'] - df['Mức đạt thực tế'])
    styles = [dict(selector="caption",
                    props=[("text-align", "center"),
                    ("font-size", "150%"),
                    ("color", 'black')])]
    df.style.set_caption('KẾ HOẠCH ĐÁNH GIÁ MỨC ĐỘ TÍCH LŨY CHUẨN ĐẦU RA HỌC KỲ THỨ NHẤT').set_table_styles(styles)
    #df.fill
    csv = convert_df(df)
    st.download_button("Tải tập tin tổng hợp", csv, "báo cáo tổng hợp học kỳ {} môn {}.csv".format(semeter,subject), "text/csv", key='download-file.csv')    
    return st.dataframe(df.style.set_caption('KẾ HOẠCH ĐÁNH GIÁ MỨC ĐỘ TÍCH LŨY CHUẨN ĐẦU RA HỌC KỲ THỨ NHẤT').set_table_styles(styles))
    
def make_df_sum(datas):
     df = []
     rs = []
     for data in datas:
          cal = data["Mức đạt thực tế"] * data["Tín chỉ"]
          df.append(data)
          rs.append(cal)
     dtf = pd.concat(df)
     sumary = np.sum(rs) / dtf["Tín chỉ"].sum()
     sumary = np.abs(np.round(sumary, 2))
     dtf["Kết quả tích lũy toàn khóa"] = ''
     dtf["Kết quả tích lũy toàn khóa"][0] = sumary
     dtf.drop(columns = dtf.columns[0], axis=1, inplace=True)
     dtf.fillna(' ')
     return dtf


          
