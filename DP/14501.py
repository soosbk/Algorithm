n=int(input())
time=[]
cost=[]
for i in range(n):
	t,c=map(int,input().split())
	time.append(t)
	cost.append(c)
	

dp=[0]*(n+1)
max_v=0
for i in range(n-1,-1,-1):
	max_time=time[i]+i
	if max_time<=n:
		dp[i]=max(cost[i]+dp[max_time],max_v)
		max_v=dp[i]
	else:
		dp[i]=max_v


print(max_v)
