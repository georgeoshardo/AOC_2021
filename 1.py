from numpy import genfromtxt
a = genfromtxt("1.txt",delimiter="/n")
q1 = sum([1 for (a,b) in zip(a[1:], a[:-1]) if (a-b) > 0])
q2 = sum([1 for (a,b) in zip([sum([a,b,c]) for a,b,c in zip(a[:-2],a[1:-1],a[2:])][1:], [sum([a,b,c]) for a,b,c in zip(a[:-2],a[1:-1],a[2:])][:-1]) if (a-b) > 0])
print(q1, q2)