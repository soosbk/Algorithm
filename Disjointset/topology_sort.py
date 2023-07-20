from collections import deque
import copy

n=int(input())
graph=[[] for i in range(n+1)]
indegree=[0]*(n+1)
time=[0]*(n+1)




for i in range(1,n+1):
	data=list(map(int,input().split()))
	time[i]=data[0]
	for j in data[1:-1]:
		indegree[i]+=1
		graph[j].append(i)



def topology_sort():
	result=copy.deepcopy(time)
	queue=deque()



	for i in range(1,n+1):
		if indegree[i]==0:
			queue.append(i)

	while queue:
		now=queue.popleft()
		for i in graph[now]:
			indegree[i]-=1
			result[i]=max(result[i],result[now]+time[i])
			if indegree[i]==0:
				queue.append(i)



	for i in range(1,n+1): print(result[i])




topology_sort()

