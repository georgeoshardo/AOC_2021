#%% 
import numpy as np
import csv
from skimage.draw import line
a = []
with open("/home/georgeos/Documents/GitHub/AOC_2021/5.txt") as file:
    reader = csv.reader(file,delimiter='\n')
    for i, row in enumerate(reader):
        a.append(row)
a = np.array([[int(x) for x in o] for o in [z.split(",") for j in [w[0].split(" -> ") for w in a] for z in j]]).reshape(500,4)
b = np.zeros((1000,1000))
def index(a):
    if a[0] <= a[2]:
        x1 = a[0]
        x2 = a[2]
    else:
        x1 = a[2]
        x2 = a[0]
    if a[1] <= a[3]:
        y1 = a[1]
        y2 = a[3]
    else:
        y1 = a[3]
        y2 = a[1]
    return (x1,x2,y1,y2)
for i in map(index,a):
    if (i[0] == (i[1])) or (i[2] == (i[3])):
        b[i[0]:i[1]+1,i[2]:i[3]+1] += 1
print(len(np.where(b > 1)[0]))
plt.figure(figsize=(10,10))
plt.imshow(b.T)


#%% 
a = []
with open("/home/georgeos/Documents/GitHub/AOC_2021/5.txt") as file:
    reader = csv.reader(file,delimiter='\n')
    for i, row in enumerate(reader):
        a.append(row)
a = np.array([[int(x) for x in o] for o in [z.split(",") for j in [w[0].split(" -> ") for w in a] for z in j]]).reshape(500,4)
b = np.zeros((1000,1000))
def index(a):
    if a[0] <= a[2]:
        x1 = a[0]
        x2 = a[2]
    else:
        x1 = a[2]
        x2 = a[0]
    if a[1] <= a[3]:
        y1 = a[1]
        y2 = a[3]
    else:
        y1 = a[3]
        y2 = a[1]
    return (x1,x2,y1,y2)
for i in a:
    b[line(*i)] += 1
print(len(np.where(b > 1)[0]))
plt.figure(figsize=(10,10))
plt.imshow(b.T)


# %%

