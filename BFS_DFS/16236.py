from collections import deque
INF=1e9

n=int(input())
graph=[]

for _ in range(n):
	graph.append(list(map(int,input().split())))


size=2
nowx,nowy=0,0
for i in range(n):
	for j in range(n):
		if graph[i][j]==9:
			nowx=i
			nowy=j
			graph[i][j]=0



dx=[1,0,-1,0]
dy=[0,1,0,-1]
	
def bfs():
	dist=[[-1]*n for _ in range(n)]
	q=deque()
	q.append((nowx,nowy))
	dist[nowx][nowy]=0
	while q:
		x,y=q.popleft()
		for i in range(4):
			nx=x+dx[i]
			ny=y+dy[i]
			if 0<=nx<n and 0<=ny<n:
				if graph[nx][ny]<=size and dist[nx][ny]==-1:
					dist[nx][ny]=dist[x][y]+1
					q.append((nx,ny))
	return dist



def find_min(dist):
	min_size=INF
	x,y=0,0
	for i in range(n):
		for j in range(n):
			if dist[i][j]!=-1 and 1<=graph[i][j]<size:
				if dist[i][j]<min_size:
					x,y=i,j
					min_size=dist[i][j]
	if min_size==INF:
		return None
	else:
		return x,y,min_size


result=0

ate=0

while True:
	value=find_min(bfs())
	if value==None:
		print(result)
		break

	else:
		nowx,nowy=value[0],value[1]
		result+=value[2]
		graph[nowx][nowy]=0
		ate+=1
		if ate>=size:
			size+=1
			ate=0
