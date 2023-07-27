from collections import deque
n,k=map(int,input().split())

data=[]
queue=[]
for i in range(n):
	data.append(list(map(int,input().split())))
	for j in range(n):
		if data[i][j]!=0: queue.append((data[i][j],0,i,j))


s,x,y=map(int,input().split())
queue.sort()
q=deque(queue)
#bfs ->queue


dx=[-1,0,1,0]
dy=[0,-1,0,1]
while q:
	virus,ctime,cx,cy=q.popleft()
	if ctime==s: break
	for i in range(4):
		nx=cx+dx[i]
		ny=cy+dy[i]
		if nx>=0 and nx<n and ny>=0 and ny<n: 
			if data[nx][ny]==0:
				data[nx][ny]=virus
				q.append((virus,ctime+1,nx,ny))


print(data[x-1][y-1])
