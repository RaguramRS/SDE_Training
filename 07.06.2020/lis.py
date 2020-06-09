def lis(arr):
	n=len(arr)
	lis=[1]*n
	for i in range(1,n):
		for j in range(0,i):
			if arr[i]>arr[j] and lis[i]<lis[j]+1:
				lis[i]=lis[j]+1
	maxm=0
	for i in range(n):
		maxm=max(maxm,lis[i])
    return maxm
print("\nLength of LIS is",lis(list(map(int,input("Enter input list:\n").split()))))
