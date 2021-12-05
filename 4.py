#%%
import csv
import numpy as np
from functools import reduce
pos = np.array([0,0])
movement = {"forward": np.array([1,0]), "down": np.array([0,1]), "up": np.array([0,-1])}
a = []
#%%
with open("4.txt") as file:
    reader = csv.reader(file,delimiter=" ")
    for i, row in enumerate(reader):
        if i > 0:
            break
        a.append(row)
b = []
with open("4.txt") as file:
    reader = csv.reader(file,delimiter=" ")
    for i, row in enumerate(reader):
        if i > 1:
            b.append(row)
        
# %%
bingo_numbers = [int(x) for x in a[0][0].split(",")]
bingo_cards = [np.array([[int(x) for x in j if (len(x)>0)] for j in b[i:i+5]]) for i in range(0,len(b),6)]
markings = [np.zeros((5,5)) for x in range(len(bingo_cards))]

def check_win(marking):
    if 5 in sum([column for column in marking.T]):
        return True
    if 5 in sum([row for row in marking]):
        return True
# %%
def play_bingo():
    for bingo_number in bingo_numbers:
        for i, card in enumerate(bingo_cards):
            markings[i] += (card == bingo_number)*1
            markings[i] = 1*(markings[i]>0)
            if check_win(markings[i]):
                return (card, markings[i], bingo_number, i)
            
# %%
win_card, win_mark, win_number, index = play_bingo()

# %%
np.sum((win_mark-1)*(-1)*win_card)*win_number

# %%
bingo_numbers = [int(x) for x in a[0][0].split(",")]
bingo_cards = [np.array([[int(x) for x in j if (len(x)>0)] for j in b[i:i+5]]) for i in range(0,len(b),6)]
markings = [np.zeros((5,5)) for x in range(len(bingo_cards))]
def play_bingo():
    for bingo_number in bingo_numbers:
        for i, card in enumerate(bingo_cards):
            if i in skip_idx:
                pass
            else:
                markings[i] += (card == bingo_number)*1
                markings[i] = 1*(markings[i]>0)
                if check_win(markings[i]):
                    return (card, markings[i], bingo_number, i)
skip_idx = []
for x in range(len(bingo_cards)):
    win_card, win_mark, win_number, index= play_bingo()
    skip_idx.append(index)
# %%
np.sum((win_mark-1)*(-1)*win_card)*win_number
