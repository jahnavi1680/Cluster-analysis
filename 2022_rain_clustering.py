# -*- coding: utf-8 -*-
"""
Created on Tue May 30 19:20:37 2023

@author: jp042
"""

#import seaborn as sns
import pandas as pd
#from pysal.lib import weights
#import geopandas as gpd
#import contextily as cx
import numpy as np
import matplotlib.pyplot as plt
#from sklearn import cluster
df = pd.read_csv(r"C:\Users\jp042\Downloads\2022_rain - 2022_rain.csv")
df['average'] = df.mean(axis=1)
df['total'] = df.sum(axis=1)
wet =[]
hp =[]
for j in range(df.shape[0]):
    count = np.sum(np.array(df.iloc[j]) > 0.25)
    hpcount = np.sum(np.array(df.iloc[j]) > 12.5)
    wet.append(count)
    hp.append(hpcount)
df['wetdays'] = wet
df['high_precip'] = hp
rainfall = ['average','total','wetdays','high_precip' ]

# Create figure and axes (this time it's 9, arranged 3 by 3)
f, axs = plt.subplots(nrows=2, ncols=2, figsize=(12, 12))
# Make the axes accessible with single indexing
axs = axs.flatten()
# Start the loop over all the variables of interest
for i, col in enumerate(rainfall):
    # select the axis where the map will go
    ax = axs[i]
    # Plot the map
    df.plot(
        column=col, 
        ax=ax, 
        scheme='Quantiles',
        linewidth=0.01, 
        cmap='Blues', 
        alpha=0.75
    )
    # Remove axis clutter
    ax.set_axis_off()
    # Set the axis title to the name of variable being plotted
    ax.set_title(col)
# Display the figure
plt.show()

