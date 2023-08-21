from collections import deque
import copy




c=int(input())
for _ in range(c):
	n=int(input())
	indegree=[0]*(n+1)
	graph=[[False]*(n+1) for _ in range(n+1)]
	t=list(map(int,input().split()))
	for i in range(n):
		for j in range(i+1,n):
			graph[t[i]][t[j]]=True
			indegree[t[j]]+=1
	m=int(input())
	for _ in range(m):
		a,b=map(int,input().split())
		if graph[a][b]:
			graph[a][b]=False
			graph[b][a]=True
			indegree[a]+=1
			indegree[b]-=1

		else:
			graph[a][b]=True
			graph[b][a]=False
			indegree[a]-=1
			indegree[b]+=1
		
	
	queue=deque()
	answer=[]
	


	for i in range(1,n+1):
		if indegree[i]==0:
			queue.append(i)

	certain=True
	cycle=False


	for i in range(n):
		if len(queue)==0:
			cycle=True # 큐가 비어있으면 사이클 발생
			break
		if len(queue)>=2:
			certain=False
			break

		now=queue.popleft()
		answer.append(now)
		for j in range(1,n+1):
			if graph[now][j]:
				indegree[j]-=1
				if indegree[j]==0:
					queue.append(j)

	
	if cycle: print("IMPOSSIBLE")
	elif certain==False: print("?")
	else: 
		for i in answer:
			print(i,end=" ")
		print()







