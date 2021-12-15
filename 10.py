#%%
import numpy as np
import csv
a = []
with open("/home/georgeos/Documents/GitHub/AOC_2021/10.txt") as file:
    reader = csv.reader(file,delimiter='\n')
    for i, row in enumerate(reader):
        a.append(row)


dirs = {
    "{": "L", "(": "L", "<": "L", "[": "L",
    "}": "R", ")": "R", ">": "R", "]": "R"
        }
complements = {
    "{": "}", "(": ")", "<": ">", "[": "]",
    "}": None, ")": None, ">": None, "]": None
}
points = {
    ")": 3, "]": 57, "}": 1197, ">": 25137, None: 0
}
ac_points = {
    "(": 1, "[": 2, "{": 3, "<": 4
}
# %%
def get_outlier(st, return_cat=False):
    rst = list(reversed(st))
    a = len(rst)
    b = len(rst)-1
    while a != b:
        a = len(rst)
        for x in range(len(rst)-1):
            if dirs[rst[x]] == dirs[rst[x+1]]:
                pass
            elif (dirs[rst[x]] != dirs[rst[x+1]]) and rst[x] == complements[rst[x+1]]:
                rst = rst[:x] + rst[x+2:]
                b = len(rst)
                break
            else:
                pass
    #print("".join([x for x in reversed(rst)]))
    for x in range(len(rst)-1):
        if (dirs[rst[x+1]] == "L") and (dirs[rst[x]] != dirs[rst[x+1]]):
            if dirs[rst[x]] == "R":
                return rst[x]
    if return_cat:
        return "".join([x for x in reversed(rst)])
    else:
        return None

p1_soln = sum([points[z] for z in [get_outlier(x[0]) for x in a]])
# %%
p2_input = [get_outlier(x[0],return_cat=True) for x in a if get_outlier(x[0],return_cat=False) == None]
# %%
ss = []
for i in p2_input:
    s = 0
    for x in reversed(i):
        s = s*5 + ac_points[x]
    ss.append(s)
# %%
p2_soln = int(np.median(sorted(ss)))