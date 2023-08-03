n=int(input())
array=list(map(int,input().split()))
dp=[1 for _ in range(n)]
cnt=0
for i in range(1,n):
	for j in range(0,i):
		if array[i]<array[j]:
			dp[i]=max(dp[i],dp[j]+1)




print(n-max(dp))
