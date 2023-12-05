import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv("2019_kbo_for_kaggle_v2.csv")

data2015 = df[df['p_year'] == 2016]

data2016 = df[df['p_year'] == 2017]

data2017 = df[df['p_year'] == 2018]

data2018 = df[df['p_year'] == 2019]

Hleader2015 = data2015.sort_values(by=['H'], ascending = False).head(10)

Hleader2016 = data2016.sort_values(by=['H'], ascending = False).head(10)

Hleader2017 = data2017.sort_values(by=['H'], ascending = False).head(10)

Hleader2018 = data2018.sort_values(by=['H'], ascending = False).head(10)

avgleader2015 = data2015.sort_values(by=['avg'], ascending = False).head(10)

avgleader2016 = data2016.sort_values(by=['avg'], ascending = False).head(10)

avgleader2017 = data2017.sort_values(by=['avg'], ascending = False).head(10)

avgleader2018 = data2018.sort_values(by=['avg'], ascending = False).head(10)

HRleader2015 = data2015.sort_values(by=['HR'], ascending = False).head(10)

HRleader2016 = data2016.sort_values(by=['HR'], ascending = False).head(10)

HRleader2017 = data2017.sort_values(by=['HR'], ascending = False).head(10)

HRleader2018 = data2018.sort_values(by=['HR'], ascending = False).head(10)

OBPleader2015 = data2015.sort_values(by=['OBP'], ascending = False).head(10)

OBPleader2016 = data2016.sort_values(by=['OBP'], ascending = False).head(10)

OBPleader2017 = data2017.sort_values(by=['OBP'], ascending = False).head(10)

OBPleader2018 = data2018.sort_values(by=['OBP'], ascending = False).head(10)

print("2015년 H TOP10 \n",Hleader2015.groupby(["H"])["batter_name"].sum().sort_index(ascending=False))

print("2016년 H TOP10 \n",Hleader2016.groupby(["H"])["batter_name"].sum().sort_index(ascending=False))

print("2017년 H TOP10 \n",Hleader2017.groupby(["H"])["batter_name"].sum().sort_index(ascending=False))

print("2018년 H TOP10 \n",Hleader2018.groupby(["H"])["batter_name"].sum().sort_index(ascending=False))

print("2015년 avg TOP10 \n",avgleader2015.groupby(["avg"])["batter_name"].sum().sort_index(ascending=False))

print("2016년 avg TOP10 \n",avgleader2016.groupby(["avg"])["batter_name"].sum().sort_index(ascending=False))

print("2017년 avg TOP10 \n",avgleader2017.groupby(["avg"])["batter_name"].sum().sort_index(ascending=False))

print("2018년 avg TOP10 \n",avgleader2018.groupby(["avg"])["batter_name"].sum().sort_index(ascending=False))

print("2015년 HR TOP10 \n",HRleader2015.groupby(["HR"])["batter_name"].sum().sort_index(ascending=False))

print("2016년 HR TOP10 \n",HRleader2016.groupby(["HR"])["batter_name"].sum().sort_index(ascending=False))

print("2017년 HR TOP10 \n",HRleader2017.groupby(["HR"])["batter_name"].sum().sort_index(ascending=False))

print("2018년 HR TOP10 \n",HRleader2018.groupby(["HR"])["batter_name"].sum().sort_index(ascending=False))

print("2015년 OBP TOP10 \n",OBPleader2015.groupby(["OBP"])["batter_name"].sum().sort_index(ascending=False))

print("2016년 OBP TOP10 \n",OBPleader2016.groupby(["OBP"])["batter_name"].sum().sort_index(ascending=False))

print("2017년 OBP TOP10 \n",OBPleader2017.groupby(["OBP"])["batter_name"].sum().sort_index(ascending=False))

print("2018년 OBP TOP10 \n",OBPleader2018.groupby(["OBP"])["batter_name"].sum().sort_index(ascending=False))



포수1 = data2018[(data2018['cp'] == '포수')].sort_values(by=['war'], ascending = False).head(1)

일루수1= data2018[(data2018['cp'] == '1루수')].sort_values(by=['war'], ascending = False).head(1)

이루수1= data2018[(data2018['cp'] == '2루수')].sort_values(by=['war'], ascending = False).head(1)

삼루수1= data2018[(data2018['cp'] == '3루수')].sort_values(by=['war'], ascending = False).head(1)

유격수1= data2018[(data2018['cp'] == '유격수')].sort_values(by=['war'], ascending = False).head(1)

좌익수1= data2018[(data2018['cp'] == '좌익수')].sort_values(by=['war'], ascending = False).head(1)

중견수1= data2018[(data2018['cp'] == '중견수')].sort_values(by=['war'], ascending = False).head(1)

우익수1= data2018[(data2018['cp'] == '우익수')].sort_values(by=['war'], ascending = False).head(1)

ans2 = pd.concat([포수1,일루수1,이루수1,삼루수1,유격수1,좌익수1,중견수1,우익수1], axis=0)



print("2018년 각 포지션별 war 1등 \n",ans2[['cp','batter_name','war']])

ex3 = df.drop(['batter_name','age','G','PA','AB','2B','3B','TB','CS','BB','HBP','GB','SO',
        'GDP','BU','fly','year','year_born','hand2','cp','tp','1B','FBP','OPS',
       'p_year','YAB','YOPS'], axis=1)

print(ex3)

corr = ex3.corrwith(ex3.salary).sort_values(ascending=False).head(2)

print("가장 연봉과 상관관계가 높은것은? \n", corr.iloc[1:])