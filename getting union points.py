# -*- coding: utf-8 -*-
"""
Created on Tue May 30 09:11:41 2023

@author: jp042
"""
import pandas as pd
loc_list = []
comb = []
for i in range(2010,2020):
    df = pd.read_excel(r"C:\Users\jp042\Downloads\summer_project\allrain.xlsx", sheet_name=format(i))
    loc = df[['X', 'Y']].values.tolist()
    loc_list.append(loc)
    comb = comb+ loc
point_set = set(map(tuple, comb))

# Convert the combined list into a set to eliminate duplicates

# Convert the set back into a list of elementary points
union_points = list(point_set)

# Display the union of elementary points
