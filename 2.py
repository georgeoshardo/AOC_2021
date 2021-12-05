import csv
import numpy as np
from functools import reduce
pos = np.array([0,0])
movement = {"forward": np.array([1,0]), "down": np.array([0,1]), "up": np.array([0,-1])}
a = []
with open("2.txt") as file:
    reader = csv.reader(file,delimiter=" ")
    for row in reader:
        a.append(row)
        
p1 = reduce(lambda x, y: x+y, [movement[m]*int(d) for m, d in a])
print(np.prod(p1))