def lcs(X,Y):
    m,n=len(X),len(Y)
    L=[[None]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0 :
                L[i][j]=0
            elif X[i-1]==Y[j-1]:
                L[i][j]=L[i-1][j-1]+1
            else:
                L[i][j]=max(L[i-1][j] ,L[i][j-1])
    return L[m][n]
print("\nLength of LCS is",lcs(input("Enter String_1: "),input("Enter String_2: ")))
