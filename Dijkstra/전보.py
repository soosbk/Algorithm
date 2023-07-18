import heapq
import sys

input=sys.stdin.readline  #한줄씩 받도록 설정변경

n,m,start=map(int,input().split())
INF=int(1e9)
graph=[[] for i in range(n+1)] #x->y=z  graph[x].append((y,z))
distance=[INF]*(n+1)

for _ in range(m):
	x,y,z=map(int,input().split())
	graph[x].append((y,z))


def dijkstra(start):
	q=[]

	heapq.heappush(q,(0,start)) #시작은 거리 0
	distance[start]=0

	while q:
		dist,now=heapq.heappop(q)
		if distance[now]<dist: # 거리 업데이트 최단거리로
			continue

		for i in graph[now]:
			cost=dist+i[1] #현재 거리랑 가까운 곳 까지 가는 거리

			if cost<distance[i[0]]:
				distance[i[0]]=cost
				heapq.heappush(q,(cost,i[0])) #새로운 경로 넣기

dijkstra(start)

count=0
d=0
print(distance)
for i in distance:
	if i!=INF:
		count+=1
		d=max(d,i)

print(count,d)


