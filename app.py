import streamlit as st
import pandas as pd
import matplotlib.pyplot as pl

data = pd.read_excel('https://raw.githubusercontent.com/jolin1215/FinalProject/main/活頁簿2.xlsx')

def assign_time_range(hours):
    if hours <= 10:
        return '0~10hr'
    elif 10 < hours <= 20:
        return '11~20hr'
    elif 20 < hours <= 30:
        return '21~30hr'
    else:
        return '30~hr'

data['時間區間'] = data['平均一個星期讀書時間'].apply(assign_time_range)

grouped_data = data.groupby(['時間區間', '生理性別']).size().unstack().fillna(0)

st.plotly_chart(grouped_data.plot(kind='line').figure)

pl.xlabel('time of range')
pl.ylabel('number of people')

st.pyplot(pl)
