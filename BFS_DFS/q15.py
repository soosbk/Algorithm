from collections import deque


n,m,k,x=map(int,input().split())
city=[[] for i in range(n+1)]
for i in range(m):
	a,b=map(int,input().split())
	city[a].append(b)


#BFS
q=deque([x])
checklist=[-1 for i in range(n+1)]
checklist[x]=0
while q:
	now=q.popleft()
	for i in city[now]:
		if checklist[i]==-1:
			checklist[i]=checklist[now]+1
			q.append(i)
	
check=False

for i in range(1,n+1):
	if checklist[i]==k:
		print(i)
		check=True

if check==False:
	print(-1)
