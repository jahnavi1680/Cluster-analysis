# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 12:23:58 2023

@author: jp042
"""

import pandas as pd
import geopandas as gpd
from sklearn import cluster
from pysal.lib import weights
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel(r"C:\Users\jp042\Downloads\summer_project\climate data\last3years.xlsx", sheet_name='rain_calculated')
dfnew = df[['X','Y']]
for i in ['rain','tmax','tmin','humid']:
    if(i=='humid'):
        df=pd.read_excel(r"C:\Users\jp042\Downloads\15all.xlsx", sheet_name='15_{}'.format(i))
        names = df.columns[[3]]
        dfnew[names] = df[names]
    elif(i=='tmin'):
        df=pd.read_excel(r"C:\Users\jp042\Downloads\15all.xlsx", sheet_name='2015_{}'.format(i))
        names = df.columns[[2,3,4]]
        dfnew[names] = df[names]
    elif(i=='tmax'):
        df=pd.read_excel(r"C:\Users\jp042\Downloads\15all.xlsx", sheet_name='2015_{}_sister'.format(i))
        names = df.columns[[-3,-2,-1]]
        dfnew[names] = df[names]
    else:
        df=pd.read_excel(r"C:\Users\jp042\Downloads\15all.xlsx", sheet_name='2015_{}'.format(i))
        names = df.columns[[3,5,6]]
        dfnew[names] = df[names]
# =============================================================================
# df = pd.read_excel(r"C:\Users\jp042\Downloads\summer_project\climate data\last5years.xlsx")
# col=['X', 'Y', 'average_rainfall', 'wet_days', 'high_days', 'average_tmax',
#        'hot_days', 'max_year', 'average_tmin', 'cold_days', 'min_year']
# dfnew[col] = df[col]
# =============================================================================
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df['X'], df['Y']))
w = weights.Queen.from_dataframe(gdf)
sagg13 = cluster.AgglomerativeClustering(n_clusters=7, connectivity=w.sparse)
# Run the clustering algorithm
#variables = 
sagg13cls = sagg13.fit(dfnew.iloc[:,[2,3,4,5,6,7,8,9]])
dfnew['sagg13cls'] = sagg13cls.labels_

groups = dfnew.groupby('sagg13cls')
plt.figure(figsize=(18,18))
for name, group in groups:
    plt.plot(group.X, group.Y, marker='o', linestyle='', markersize=18, label=name)

plt.legend()
#with pd.ExcelWriter(r"C:\Users\jp042\Downloads\last10years (1).xlsx", mode='a') as writer:
    #dfnew.to_excel(writer, sheet_name='all', index=False)

# =============================================================================
# for i in range(5):
#     grp = groups.get_group(i).describe()
#     with pd.ExcelWriter(r"C:\Users\jp042\Downloads\last3years.xlsx", mode='a') as writer:
#         grp.to_excel(writer, sheet_name='cluster_{}'.format(i), index=False)
# =============================================================================
