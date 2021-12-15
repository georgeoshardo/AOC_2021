#%%
import numpy as np
import csv
a = []
with open("/home/georgeos/Documents/GitHub/AOC_2021/8.txt") as file:
    reader = csv.reader(file,delimiter='\n')
    for i, row in enumerate(reader):
        a.append(row)
# %%
p1 = [x[0].split(" | ")[1].split(" ") for x in a]
p2 = [x[0].split(" | ")[0].split(" ") for x in a]
p1_soln = sum([1 for j in [x for y in p1 for x in y] if len(j) in [2,3,4,7]])
# %%
def str2set(str):
    return set([x for x in str])
def get_line_sum(diag, output):
    #diag = ["acedgfb", "cdfbe", "gcdfa", "fbcad", "dab", "cefabd", "cdfgeb", "eafb", "cagedb", "ab"]
    test = set(["".join(sorted([x for x in y])) for y in diag])
    unknown = test
    known = set()
    for e in unknown:
        if len(e) == 2:
            one = e
            known.add(one)
        elif len(e) == 4:
            four = e
            known.add(four)
        elif len(e) == 3:
            seven = e
            known.add(seven)
        elif len(e) == 7:
            eight = e
            known.add(e)
        else:
            pass
    unknown -= known
    for e in unknown:
        if (len(e) == 6) and str2set(four).issubset(str2set(e)):
            nine = e
            known.add(nine)
    unknown -= known
    for e in unknown:
        if (len(e) == 6) and str2set(one).issubset(str2set(e)):
            zero = e
            known.add(zero)
    unknown -= known
    for e in unknown:
        if (len(e) == 6):
            six = e
            known.add(six)
    unknown -= known
    for e in unknown:
        if (len(e) == 5) and str2set(e).issubset(str2set(six)):
            five = e
            known.add(five)
    unknown -= known
    for e in unknown:
        if str2set(e).issubset(str2set(nine)):
            three = e
            known.add(three)
    unknown -= known
    for e in unknown:
        two = e
        known.add(two)
    unknown -= known
    numdict = {one: 1, two: 2, three: 3, four: 4, five: 5, six: 6, seven: 7, eight: 8, nine: 9, zero: 0}

    outputs = ["".join(sorted([x for x in y])) for y in output]
    return int("".join([str(z) for z in [numdict[x] for x in outputs]]))
# %%
print(sum([get_line_sum(x,y) for x,y in zip(p2,p1)]))

# %%
