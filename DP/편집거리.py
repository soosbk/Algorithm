a=input()
b=input()

n=len(a)+1
m=len(b)+1
dp=[[0]*m for _ in range(n)]


for i in range(n):
	for j in range(m):
		if i==0: dp[i][j]=j
		elif j==0: dp[i][j]=i


for i in range(1,n):
	for j in range(1,m):
		if a[i-1]==b[j-1]:
			dp[i][j]=dp[i-1][j-1]
		else:
			dp[i][j]=min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1
print(dp[i][j])
