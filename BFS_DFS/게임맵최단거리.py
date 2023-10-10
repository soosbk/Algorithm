from collections import deque
def solution(maps):
    n=len(maps)
    m=len(maps[0])
    if n==1 and m==1: return 1
    INF=int(1e9)
    distance=[[INF]*m for _ in range(n)]
    distance[0][0]=1
    q=deque([[0,0]])
    while q:
        x,y=q.popleft()
        t=distance[x][y]
        if x+1<n and maps[x+1][y]==1 and t+1<distance[x+1][y]:
            q.append([x+1,y])
            distance[x+1][y]=t+1
        if y+1<m and maps[x][y+1]==1 and t+1<distance[x][y+1]:
            q.append([x,y+1])
            distance[x][y+1]=t+1
        if x-1>=0 and maps[x-1][y]==1 and t+1<distance[x-1][y]:
            q.append([x-1,y])
            distance[x-1][y]=t+1
        if y-1>=0 and maps[x][y-1]==1 and t+1<distance[x][y-1]:
            q.append([x,y-1])
            distance[x][y-1]=t+1

            
    if distance[n-1][m-1]==INF: return -1
    return distance[n-1][m-1]
