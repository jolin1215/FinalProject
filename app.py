!pip install matplotlib
!pip install pandas

import pandas as pd
import matplotlib.pyplot as plt

# 讀取Excel檔案
data = pd.read_excel('活頁簿2.xlsx')

# 定義函式，根據讀書時間分配到對應的區間
def assign_time_range(hours):
    if hours <= 10:
        return '0~10hr'
    elif 10 < hours <= 20:
        return '11~20hr'
    elif 20 < hours <= 30:
        return '21~30hr'
    else:
        return '30~hr'

# 新增讀書時間區間欄位
data['時間區間'] = data['平均一個星期讀書時間'].apply(assign_time_range)

# 以時間區間和性別分組，計算每個時間區間的人數
grouped_data = data.groupby(['時間區間', '生理性別']).size().unstack().fillna(0)

# 繪製雙曲線圖
grouped_data.plot(kind='line')

# 設定圖表標籤等
plt.xlabel('time of range')
plt.ylabel('number of people')

# 顯示圖表
plt.show()
