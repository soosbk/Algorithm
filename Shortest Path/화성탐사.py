import heapq

t=int(input())
INF=int(1e9)

for _ in range(t):
	m=int(input())
	array=[]
	distance=[[INF]*m for _ in range(m)]
	for _ in range(m):
		array.append(list(map(int,input().split())))


	q=[]
	q.append((array[0][0],0,0))
	dx=[1,0,-1,0]
	dy=[0,1,0,-1]

	while q:
		dis,x,y=heapq.heappop(q)
		if distance[x][y]<dis: continue
		for i in range(4):
			nx=x+dx[i]
			ny=y+dy[i]

			if nx<0 or nx>=m or ny<0 or ny>=m: continue
			cost=dis+array[nx][ny]
			if cost<distance[nx][ny]:
				distance[nx][ny]=cost
				heapq.heappush(q,(cost,nx,ny))

	print(distance[m-1][m-1])
