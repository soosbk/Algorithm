import copy


graph=[[] for _ in range(4)]
for i in range(4):
	data=list(map(int,input().split()))
	for j in range(0,len(data),2):
		graph[i].append([data[j],data[j+1]-1])




dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,-1,-1,-1,0,1,1,1]


answer=0
def turn(d):
	return (d+1)%8

def find(graph,idx):
	for i in range(4):
		for j in range(4):
			if graph[i][j][0]==idx:
				return (i,j)

	return None

def move_all_fishes(graph,now_x,now_y):
	for fish in range(1,17):
		position=find(graph,fish)

		if position!=None:
			x,y=position[0],position[1]
			direction=graph[x][y][1]
			for _ in range(8):
				nx=x+dx[direction]
				ny=y+dy[direction]

				if 0<=nx<4 and 0<=ny<4:
					if not (nx==now_x and ny==now_y):
						graph[x][y][1]=direction					
						graph[x][y],graph[nx][ny]=graph[nx][ny],graph[x][y]
						break


				direction=turn(direction)




def shark_position(graph,nowx,nowy):
	positions=[]
	d=graph[nowx][nowy][1]
	for i in range(4):
		nowx+=dx[d]
		nowy+=dy[d]

		if 0<=nowx<4 and 0<=nowy<4:
			if graph[nowx][nowy][0]!=-1:
				positions.append((nowx,nowy))


	return positions




def dfs(graph,x,y,total):
	global answer
	graph=copy.deepcopy(graph)

	total+=graph[x][y][0]
	graph[x][y][0]=-1
	move_all_fishes(graph,x,y)
	positions=shark_position(graph,x,y)

	if len(positions)==0:
		answer=max(answer,total)
		return 


	for sx,sy in positions:
		dfs(graph,sx,sy,total)


dfs(graph,0,0,0)
print(answer)
