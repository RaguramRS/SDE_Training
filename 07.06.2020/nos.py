from itertools import combinations
from numpy import prod
n=int(input("Enter n:\n"))
li=list(map(int,input("Enter list elemnets:\n").split()))
k=int(input("Enter k:\n"))
summ=0
for i in range(1,n+1):
	for j in list(combinations(li,i)):
		if prod(j)<=k:
			summ+=1
print("\nNumber of sub-sequences those product lesser than {} are {}".format(k,summ))
