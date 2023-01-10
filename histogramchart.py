import matplotlib.pyplot as plt
import streamlit as st
#import pandas as pd

def histogram_bart(data):
    st.set_option('deprecation.showPyplotGlobalUse', False)
    min_ylim, max_ylim = plt.ylim()
    plt.subplot()
    data.hist(color='#86bf91', zorder=2, rwidth=0.9)
    plt.text(data.mean()*1.1, max_ylim*0.9, 'Trung bình: {:.2f}'.format(data.mean()),
            fontsize = 12,
            color ='red',
            ha ='center',
            va ='top',
            alpha = 0.7)
    plt.ylabel("Số sinh viên")
    plt.xlabel("Điểm")
    st.pyplot()
    
    