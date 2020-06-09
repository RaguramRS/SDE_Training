def longestRepeatedSubSeq(str):
	n=len(str)
	dp=[[0 for i in range(n+1)] for j in range(n+1)]
	for i in range(1,n+1):
		for j in range(1,n+1):
			if str[i-1]==str[j-1] and i!=j:
				dp[i][j]=1+dp[i-1][j-1]
			else:
				dp[i][j]=max(dp[i][j-1],dp[i-1][j])
	res,i,j='',n,n
	while i>0 and j>0:
		if dp[i][j]==dp[i-1][j-1]+1:
			res+=str[i-1]
			i-=1
			j-=1
		elif dp[i][j]==dp[i-1][j]:
			i-=1
		else:
			j-=1
	return ''.join(reversed(res))
print("\nLongest Repeated Subsequence is",longestRepeatedSubSeq(input("Enter input String: ")))
