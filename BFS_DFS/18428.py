from itertools import combinations



def bfs(graph,teacher,case):
	dx=[1,0,-1,0]
	dy=[0,1,0,-1]
	for t in teacher:
		for d in range(4):
			nx=t[0]+dx[d]
			ny=t[1]+dy[d]
				
			while 0<=nx<len(graph) and 0<=ny<len(graph) and graph[nx][ny]!='T':
				if graph[nx][ny]=='S':
					return False
				if (nx,ny) in case: break
				nx+=dx[d]
				ny+=dy[d]
				
	return True




n=int(input())
graph=[]
blank=[]
teacher=[]


for i in range(n):
	data=list(map(str,input().split()))
	for j in range(n):
		if data[j]=="X":
			blank.append((i,j))
		elif data[j]=='T':
			teacher.append((i,j))



	graph.append(data)

answer=False
all_case=list(combinations(blank, 3))
a=False
for case in all_case:
	if bfs(graph,teacher,case):
		a=True
		break
		
if a: print("YES")
else: print("NO")



