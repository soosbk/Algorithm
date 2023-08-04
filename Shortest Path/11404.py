n=int(input())
m=int(input())
INF=int(1e9)

costs=[[INF]*(n+1) for _ in range((n+1))]
for i in range(m):
	a,b,c=map(int,input().split())
	costs[a][b]=min(c,costs[a][b])
for i in range(n+1):
	costs[i][i]=0

for k in range(1,n+1):
	for i in range(1,n+1):
		for j in range(1,n+1):
			costs[i][j]=min(costs[i][j],costs[i][k]+costs[k][j])




for i in range(1,n+1):
	for j in range(1,n+1):
		if costs[i][j]==INF: print(0,end=" ")
		else: print(costs[i][j],end=" ")
	print()
