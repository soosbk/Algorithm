import heapq

n,m=map(int,input().split())
array=[[] for _ in range(n+1)]
distance=[0]*(n+1)
visit=[False]*(n+1)
for i in range(m):
	a,b=map(int,input().split())
	array[a].append(b)
	array[b].append(a)

q=[]
heapq.heappush(q,(0,1)) #시작은 거리 0
distance[1]=0
visit[1]=True
while q:
	dis,now=heapq.heappop(q)
	for n in array[now]:
		if visit[n]==False:
			distance[n]=max(dis+1,distance[n])
			heapq.heappush(q,(distance[n],n))
			visit[n]=True

dis=max(distance)
cnt=distance.count(dis)
node=distance.index(dis)

print(node, " ",dis," ",cnt)


