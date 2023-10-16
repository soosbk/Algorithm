from collections import deque

n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(input()))
visited=[[int(1e9)]*m for _ in range(n)]
dx=[1,0,0,-1]
dy=[0,1,-1,0]
answer=int(1e9)
q=deque([[0,0,1]])
visited[0][0]=1
while q:
    x,y,time=q.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<n and 0<=ny<m and graph[nx][ny]=='1' and visited[nx][ny]>time+1:
            q.append([nx,ny,time+1])
            visited[nx][ny]=time+1



print(visited[n-1][m-1])
