import copy
n,l,r=map(int,input().split())
idx=0
s=0
cnt=0
change=[]
checklist=[[-1]*n for _ in range(n)]
def dfs(graph,x,y):
	global checklist
	global cnt
	global change
	global s


	try:
		if y<n-1 and l<=abs(graph[x][y+1]-graph[x][y])<=r and checklist[x][y+1]<idx:
				checklist[x][y+1]=idx
				change.append((x,y+1))
				s+=graph[x][y+1]
				cnt+=1
				dfs(graph,x,y+1)
	except:
		pass


	try:
		if x<n-1 and l<=abs(graph[x+1][y]-graph[x][y])<=r and checklist[x+1][y]<idx:
				checklist[x+1][y]=idx
				change.append((x+1,y))
				s+=graph[x+1][y]
				cnt+=1
				dfs(graph,x+1,y)
	except:
		pass


	try:
		if y>0 and l<=abs(graph[x][y-1]-graph[x][y])<=r and checklist[x][y-1]<idx:
				checklist[x][y-1]=idx
				change.append((x,y-1))
				s+=graph[x][y-1]
				cnt+=1
				dfs(graph,x,y-1)
	except:
		pass

	try:
		if x>0 and l<=abs(graph[x-1][y]-graph[x][y])<=r and checklist[x-1][y]<idx:
				checklist[x-1][y]=idx
				change.append((x-1,y))
				s+=graph[x-1][y]
				cnt+=1
				dfs(graph,x-1,y)
	except:
		pass





graph=[]
answer=0
for _ in range(n):
	graph.append(list(map(int,input().split())))

while True:
	move=False
	new_graph=copy.deepcopy(graph)
	for i in range(n):
		for j in range(n):
			idx+=1
			change=[(i,j)]
			cnt=1
			s=graph[i][j]
			checklist[i][j]=idx
			dfs(graph,i,j)
			if cnt>1:
				move=True
				s//=cnt
				for x,y in change:
					new_graph[x][y]=s

	if move==False:
		break
	answer+=1
	graph=copy.deepcopy(new_graph)


print(answer)
