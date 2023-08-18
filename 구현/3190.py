from collections import deque

n=int(input())
k=int(input())
array=[[0]*(n+1) for _ in range(n+1)]

for _ in range(k):
	x,y=map(int,input().split())
	array[x][y]=1 #사

l=int(input())
info=[0]*10001
for _ in range(l):
	s, i=input().split()
	info[int(s)+1]=i


dx=[0,1,0,-1]
dy=[1,0,-1,0]


x=1
y=1
array[1][1]=2
second=1
direction=0
snack=deque([(1,1)])
while 1:
	if info[second]!=0:
		if info[second]=='L':
			direction=(direction+3)%4


		elif info[second]=='D':
			direction=(direction+1)%4

	nx=x+dx[direction]
	ny=y+dy[direction]

	



	if nx<=0 or nx>n or ny<=0 or ny>n or array[nx][ny]==2: break
	if array[nx][ny]==0: 
		a=snack.pop()
		array[a[0]][a[1]]=0

	else: array[nx][ny]=0
	snack.appendleft((nx,ny))
	array[nx][ny]=2

	x=nx
	y=ny
		
	second+=1


print(second)

