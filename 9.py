#%% 
import numpy as np
from numpy import genfromtxt
import csv
from scipy.signal import argrelextrema
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops_table
a = []
with open("/home/georgeos/Documents/GitHub/AOC_2021/9.txt") as file:
    reader = csv.reader(file,delimiter='\n')
    for i, row in enumerate(reader):
        a.append(row)
b = []
for l in a:
    b.append([int(x) for x in l[0]])
b = np.array(b)
expanded_b = np.zeros((102,102))
expanded_b[1:101,1:101] = b
expanded_b[0,:] = expanded_b[2,:]
expanded_b[-1,:] = expanded_b[-3,:]
expanded_b[:,0] = expanded_b[:,2]
expanded_b[:,-1] = expanded_b[:,-3]
#%%

# %%
b_diff_0 = (argrelextrema(expanded_b, np.less,axis=0))
b_diff_1 = (argrelextrema(expanded_b, np.less,axis=1))
b_maxima = np.zeros((102,102))
b_maxima[b_diff_0] +=1
b_maxima[b_diff_1] +=1
part_1 = np.sum(b * (b_maxima == 2)[1:-1,1:-1]) + np.unique(b_maxima,return_counts=True)[-1][-1]
# %%
# %%
basin_edges = np.invert(b == 9)
basin_labels = label(basin_edges,connectivity=1)
basin_sizes = sorted(regionprops_table(basin_labels, properties=["area"])["area"])
part_2 = basin_sizes[-1]*basin_sizes[-2]*basin_sizes[-3]
# %%
