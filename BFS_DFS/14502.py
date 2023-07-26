n,m=map(int,input().split())

graph=[]
for _ in range(n):
	graph.append(list(map(int,input().split())))

temp=[[0]*m for _ in range(n)]
#DFS ->stack


result=0

def cnt(): # 빈칸 세기
	score=0
	for i in range(n):
		for j in range(m):
			if temp[i][j]==0: score+=1

	return score




def virus(x,y): #바이러스 퍼지도록
	global result
	dx=[-1,0,1,0]
	dy=[0,-1,0,1]
	for i in range(4):
		new_x=x+dx[i]
		new_y=y+dy[i]

		if new_y<m and new_y>=0 and new_x<n and new_x>=0: 
			if temp[new_x][new_y]==0:
				temp[new_x][new_y]=2
				virus(new_x,new_y)
		





# 0에 벽 설치할 수 있는 모든 경우의수 -> 그 때 바이러스가 최대 어디까지 퍼지는 지 계산 -> 최솟값 찾아서 반환
def dfs(count):
	global result
	

	if count==3:
		for i in range(n):
			for j in range(m):
				temp[i][j]=graph[i][j]
		for i in range(n):
			for j in range(m):
				if temp[i][j]==2: virus(i,j)
		result=max(cnt(),result)
		return 
	
	for i in range(n):
		for j in range(m):
			if graph[i][j]==0:
				graph[i][j]=1
				count+=1
				dfs(count)
				graph[i][j]=0
				count-=1





dfs(0)
print(result)
