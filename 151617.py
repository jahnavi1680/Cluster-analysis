# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 12:02:55 2023

@author: jp042
"""

import pandas as pd
import numpy as np
import openpyxl
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.neighbors import NearestNeighbors
lis= ['A','B','C','D','E','F','H','J','K','L','M','N','O']
final_sec=pd.DataFrame()
all_list=[]
for sheet in lis:
    df = pd.read_excel(r"C:\Users\jp042\Downloads\iridata.xlsx",sheet_name=sheet)
    for i in df['Lane Number'].unique():
        dfd =df[df['Lane Number']==i]
        dfd.dropna(inplace=True)
# =============================================================================
#         plt.scatter(df[df['Lane Number']==i].index,df[df['Lane Number']==i]['16-15diff'])
#         plt.show()
# =============================================================================
        data = np.array(dfd['16-15diff']).reshape(-1,1)
        neigh = NearestNeighbors(n_neighbors=2)
        nbrs = neigh.fit(data)
        distances, indices = nbrs.kneighbors(data)
        distances = distances[:,1]
        for k in np.arange(0.5, 2.01, 0.01):
            if(np.where(distances>k)[0].size<5):
                q=np.delete(data,np.where(distances>k))
                break
            else:
                continue
# =============================================================================
#         plt.scatter(pd.DataFrame(q).index,q)
#         plt.show()
# =============================================================================
        subset_indices = dfd.index[dfd['16-15diff'].isin(q)].tolist()
        df_subset = dfd.loc[subset_indices]
        data = np.array(df_subset['16-15diff']).reshape(-1, 1)
        dbscan = DBSCAN(eps=0.5, min_samples=20)
        clusters = dbscan.fit_predict(data)
        df_subset['clusters']=clusters.tolist()
        outliers = df_subset[df_subset['clusters']==-1]['16-15diff']
        inliers = df_subset[df_subset['clusters']!=-1]['16-15diff']
        if(outliers.size<10):
            df_subset=df_subset.drop(df_subset[df_subset['clusters']==-1].index)
            outliers = df_subset[df_subset['clusters']==-1]['16-15diff']
# =============================================================================
#         plt.scatter(df_subset[df_subset['clusters']!=-1].index, inliers, color='blue', label='inliers')
#         plt.scatter(df_subset[df_subset['clusters']==-1].index, outliers, color='orange', label='outliers')
#         plt.show()
# =============================================================================
        print(outliers.mean()-inliers.mean())
        final_sec=pd.concat([final_sec,df_subset])
    all_list.append(final_sec)
    