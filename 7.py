#%%
import numpy as np
from numpy import genfromtxt
a = genfromtxt("/home/georgeos/Documents/GitHub/AOC_2021/7.txt",delimiter=",")
print(sum(abs(a-np.median(a))))
# %%
a
# %%
def sum_n(n):
    return n*(n+1)/2
# %%
sum(sum_n(abs(a-x)))
print(min([sum(sum_n(abs(a-x))) for x in range(1000)]))
# %%
