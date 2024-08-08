# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 08:14:34 2023

@author: jp042
"""
import pandas as pd
df_list = []
#df =pd.read_excel(r"C:\Users\jp042\Jahnavi\123r.xlsx")
#groups = df.groupby('Section Name')
#lis = df['Section Name'].unique()
#for i in lis:
    #df1= groups.get_group(i)
    #print(df1['Survey Date'].nunique())
    
condition = lambda x: x['Survey Date'].nunique() > 1

# Apply the filter to get the new DataFrame with groups that satisfy the condition
#filtered_df = df.groupby('Section Name').filter(condition)
#filtered_df = pd.read_csv(r"C:\Users\jp042\Jahnavi\rararaugh.csv")
# =============================================================================
# lis = filtered_df['Section Name'].unique()
# grp = filtered_df.groupby('Section Name')
# =============================================================================
# =============================================================================
# for i in lis:
#     df1= grp.get_group(i)
#     lanes = df1['Lane Number'].unique()
#     lgrp = df1.groupby('Lane Number')
# =============================================================================
#final_df = filtered_df.groupby(['Section Name', 'Lane Number', 'Start Chainage']).filter(condition)
df =pd.read_csv(r"C:\Users\jp042\Jahnavi\final.csv")
col=['NHCode', 'Section Code', 'Section Name', 'Start Chainage', 'End Chainage', 'Direction', 'Lane Number', 'Latitude', 'Longitude', 'Regional Office', 'State Name', 'Entrusted To']
print('gadida')
grp = df.groupby(['Section Name', 'Lane Number', 'Start Chainage','Survey Date'])
print('gadida2')

#print(df.head())
for i in df['Section Name'].unique():
#for i in ['Ahmedabad-Vadodara']:
    print(i)
    secdf = pd.DataFrame()
    #print(secdf.head())
    dfnew = df.loc[df['Section Name'] == i]
    
    #print(dfnew.head())
    for j in dfnew['Lane Number'].unique():
    #for j in ['L1']:
        df1 = dfnew.loc[dfnew['Lane Number'] == str(j)]
        print(j)
        print('gfgytcftvgbhjjjfdesrfgchbjtfewa,jbhxdjwhbd ')
        #print(df1.head())
        for k in df1['Start Chainage'].unique():
        #for k in [6800,6900]:
            df_new = pd.DataFrame()
            df2 = df1.loc[dfnew['Start Chainage'] ==k]
            df_new[col]=df2[col].head(1)
            print(k)
            #print('df2')
            #print(df2.head())
            #print('df_new')
            #print(df_new.iloc[0])
            for l in df2['Survey Date'].unique():
                print(l)
                #df_new[['{}iri'.format(l),'{}speed'.format(l)]]=grp.get_group((i,j,k,l))[['LaneIri','Speed']]
                df_new.loc[:, '{}iri'.format(l)]=df2.loc[df2['Survey Date'] == l]['LaneIri'].mean()
                df_new.loc[:, '{}speed'.format(l)] = df2.loc[df2['Survey Date'] == l]['Speed'].mean()
                df_new[l]=l
                #df_new['Year']=df2.loc[df2['Survey Date'] == l]['year']
                #print(df_new.head())
                #print(df_new.iloc[0])
            secdf = pd.concat([secdf,df_new])
             #print(secdf.head())
    df_list.append(secdf)
# 
# =============================================================================
