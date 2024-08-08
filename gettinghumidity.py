# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 22:13:16 2023

@author: jp042
"""

import pandas as pd
import numpy as np
import os
from statistics import mean
every=pd.DataFrame()
def get_decimal_part(column):
    return column - column.astype(int)
# Specify the folder path
folder_path = r"C:\Users\jp042\Downloads\2017 humidity"
pointfile = r"C:\Users\jp042\Downloads\summer_project\climate data\POINTS.csv"
points = pd.read_csv(pointfile)
x = points['X'].values.tolist()
y = points['Y'].values.tolist()
final_pointslist = points[['X','Y']].values.tolist()
# Loop over the files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        # Perform actions on the file
        df = pd.read_excel(file_path)
        #df=df.head(50)
        decimal_part = get_decimal_part(df['LAT'])
        mask = decimal_part == 0.25
        dfp=pd.DataFrame()
        dfp = df.loc[mask]
        decimal_part = get_decimal_part(dfp['LON'])
        mask = decimal_part == 0.25
        dfp = dfp.loc[mask]
        #print(len(dfp))
        dfp.drop(dfp.index[((dfp['LON']+0.25).isin(x) == False)&((dfp['LAT']+0.25).isin(y) == False)], axis=0, inplace=True)
        loc = dfp[['LON', 'LAT']].values.tolist()
        #print(len(loc))
        all_df =pd.DataFrame()
        new_df=pd.DataFrame(columns=['X', 'Y','maxhum','minhum','avghum'])
        for i in loc:
            sum=[0] * 366
            
            new_df[['X','Y']]=[list(np.array(i)+np.array([0.25,0.25]))]
            lb=list(np.array(i))
            rb = list(np.array(i)+np.array([0.5,0]))
            lt= list(np.array(i)+np.array([0,0.5]))
            rt = list(np.array(i)+np.array([0.5,0.5]))
            for j in [lb,rb,lt,rt]:
                if(((df['LON'] == j[0]) & (df['LAT'] == j[1])).sum()!=0):
                    h=1
                    subdf=df[(df['LON']==j[0])&(df['LAT']==j[1])] 
                    #print(mean(subdf['QV2M']))
                    sum = list(np.array(sum) +np.array(subdf['RH2M']))
                    #print(h+2)
                else:
                    h=0 
                    break
            if(h==0):
                #print('wtf')
                continue
# =============================================================================
#             for j in [lb, rb, lt, rt]:
#                 try:
#                     subdf = df[(df['LON'] == j[0]) & (df['LAT'] == j[1])]
#                     sum = list(np.array(sum) + np.array(subdf['QV2M']))
#                 except:
#                     continue
# =============================================================================
            #print(h)
            print('abrakadabra gili chu')
            
            sum_values = list(np.array(sum)/4)
            #print(sum[0])
            #new_df[column_names]=list(np.array(sum) +np.array(subdf['QV2M']))
            new_df.at[0, 'maxhum'] = max(sum_values)
            new_df.at[0, 'minhum'] = min(sum_values)
            new_df.at[0, 'avghum'] = mean(sum_values)
            new_df[['X','Y']].loc[0]=list(np.array(i)+np.array([0.25,0.25]))
            print('achu')
            all_df=pd.concat([all_df,new_df])
            all_df.drop_duplicates()
        every = pd.concat([every,all_df])
        print('what')
        print(every)
# =============================================================================
#                 linedf =pd.DataFrame(subdf['QV2M'].values.reshape(1, -1)).transpose()
#                 df.columns = range(1, 366)
#                 linedf.columns = range(1, 366)
#                 linedf['X']=j[0]
#                 linedf['Y']=j[1]
# =============================================================================
td=every.drop_duplicates()
td=td.reset_index()
pointlist = td[['X','Y']].values.tolist()
f=td.drop([index for index, element in enumerate(pointlist) if element not in final_pointslist])
f.to_csv(r"C:\Users\jp042\Downloads\2017 humidity\17final.csv")