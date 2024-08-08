# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 20:15:26 2023

@author: jp042
"""
import pandas as pd
inp = str(input('enter ur variable:'))
output_file = r"C:\Users\jp042\Downloads\last5years.xlsx"
df = pd.read_excel(r"C:\Users\jp042\Downloads\last5years.xlsx", sheet_name='2020_tmax')
dfnew = df[['X', 'Y']].copy()
if(inp == 'rain'):
    dfnew['average_rainfall']=0
    dfnew['wet_days']=0
    dfnew['high_days']=0
    for i in range(2013, 2023):
        df = pd.read_excel(r"C:\Users\jp042\Downloads\last10years.xlsx", sheet_name='{}.rain'.format(i))
        dfnew['average_rainfall'] = dfnew['average_rainfall'].copy() +df['average']
        dfnew['wet_days'] = dfnew['wet_days'].copy() + df['wetdays']
        dfnew['high_days'] = dfnew['high_days'].copy() + df['high_precip']
       
    dfnew[['average_rainfall','wet_days','high_days']] = dfnew[['average_rainfall','wet_days','high_days']] / 10
    
    with pd.ExcelWriter(output_file, mode='a') as writer:
        dfnew.to_excel(writer, sheet_name='rain_calculated', index=False)
        
elif(inp == 'tmin'):
    dfnew = dfnew[['X','Y']].copy()
    dfnew['average_tmin']=0
    dfnew['cold_days']=0
    dfnew['min_year']=0
    for i in range(2013, 2023):
        df = pd.read_excel(r"C:\Users\jp042\Downloads\last10years.xlsx", sheet_name='{}_tmin'.format(i))
        dfnew['average_tmin'] = dfnew['average_tmin'].copy() +df['minaverage']
        dfnew['cold_days'] = dfnew['cold_days'].copy() + df['colddays']
        dfnew['min_year'] = dfnew['min_year'].copy() + df['yearlymin']
    dfnew[['average_tmin','cold_days','min_year']] = dfnew[['average_tmin','cold_days','min_year']] / 10
    
    with pd.ExcelWriter(output_file, mode='a') as writer:
        dfnew.to_excel(writer, sheet_name='tmin_calculated', index=False)
    
elif(inp == 'tmax'):
    dfnew = dfnew[['X','Y']].copy()
    dfnew['average_tmax']=0
    dfnew['hot_days']=0
    dfnew['max_year']=0
    for i in range(2018, 2023):
        df = pd.read_excel(r"C:\Users\jp042\Downloads\last5years.xlsx", sheet_name='{}_tmax'.format(i))
        dfnew['average_tmax'] = dfnew['average_tmax'].copy() +df['maxaverage']
        dfnew['hot_days'] = dfnew['hot_days'].copy() + df['hotdays']
        dfnew['max_year'] = dfnew['max_year'].copy() + df['yearlymax']
    dfnew[['average_tmax','hot_days','max_year']] = dfnew[['average_tmax','hot_days','max_year']] / 5
    
    with pd.ExcelWriter(output_file, mode='a') as writer:
        dfnew.to_excel(writer, sheet_name='tmax_calculated', index=False)
    