def __gcd(a,b): 
	if a==0 or b==0:
	    return 0
	if a==b:
	    return a 
	if a>b: 
		return __gcd(a-b,b) 
	return __gcd(a,b-a) 
def coprime(a,b):
	if __gcd(a,b)==1: 
		return False 
	else: 
		return True
n=int(input())                   #4
a=list(map(int,input().split())) #16 3 2 9
b=list(map(int,input().split())) #12 18 13 4
ct=0
for i in sorted(a):
    for j in b:
        if coprime(i,j) and j>i:
            ct+=1
print("\nMaximum score received by Mr.Yagami:",ct)
