n=int(input())
dp=[]

for i in range(n):
	dp.append(list(map(int,input().split())))



answer=0
for i in range(1,n):
	for j in range(i+1):
		if j==0: leftup=0
		else: leftup=dp[i-1][j-1]
		if i==j: leftdown=0
		else: leftdown=dp[i-1][j]
		dp[i][j]=dp[i][j]+max(leftdown,leftup)
		
print(max(dp[n-1]))
