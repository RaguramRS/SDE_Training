def knapSack(W,wt,val,n):
    K=[[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w]=0
            elif wt[i-1]<=w:
                K[i][w]=max(val[i-1]+K[i-1][w-wt[i-1]],K[i-1][w])
            else:
                K[i][w]=K[i-1][w]
    return K[n][W]
val=list(map(int,input("Enter val_list:\n").split()))
wt=list(map(int,input("Enter wt_list:\n").split()))
W=int(input("Enter W:\n"))
n=len(val)
print("\nMaximum value using KNAPSACK is",knapSack(W,wt,val,n))
