n,m=map(int,input().split())
grade=[[] for _ in range(n+1)]
INF=int(1e9)

for i in range(m):
	a,b=map(int,input().split())
	grade[a].append(b)

costs=[[INF]*(n+1) for _ in range(n+1)]

for k in range(1,n+1):
	for i in range(1,n+1):
		for t in grade[i]:
			costs[i][t]=1
		for j in range(1,n+1):
			costs[i][j]=min(costs[i][j],costs[i][k]+costs[k][j])
answer=0

for i in range(1,n+1):
	cnt=0
	for j in range(1,n+1):
		if costs[i][j]!=INF or costs[j][i]!=INF:
			cnt+=1

	if n-1==cnt: answer+=1


print(answer)
