parents=[]
for i in range(51):
	t=[]
	for j in range(51):
		t.append([i,j])
	parents.append(t)
values=[[0]*51 for _ in range(51)]
	
def update_v(b,value):
	for i in range(1,51):
		for j in range(1,51):
			if find([i,j],parents)==b:
				values[i][j]=value

def find(a,parents):
	if parents[a[0]][a[1]]!=a:
		parents[a[0]][a[1]]=find(parents[a[0]][a[1]],parents)
	return parents[a[0]][a[1]]

def union(a,b):
	global parents
	global values

	a=find(a,parents)
	b=find(b,parents)
	parents[b[0]][b[1]]=parents[a[0]][a[1]]
	
	if values[a[0]][a[1]]!=0: values[b[0]][b[1]]=values[a[0]][a[1]]
	else: values[a[0]][a[1]]=values[b[0]][b[1]]
	update_v(a,values[a[0]][a[1]])
	update_v(b,values[a[0]][a[1]])
	

def solution(commands):
	answer = []
	global parents
	global values
	for command in commands:
		lst=command.split(" ")
		if lst[0]=="UPDATE":
			if len(lst)==4: #값 변경
				new_p=find([int(lst[1]),int(lst[2])],parents)
				for i in range(1,51):
					for j in range(1,51):
						if new_p==find([i,j],parents): 
							values[i][j]=lst[3]
				else:
					update_v(new_p,lst[3])
							
			else: #모든 셀
				for i in range(1,51):
					for j in range(1,51):
						if values[i][j]==lst[1]:
							values[i][j]=lst[2]


		elif lst[0]=="MERGE":
			if find([int(lst[1]),int(lst[2])],parents)==find([int(lst[3]),int(lst[4])],parents): continue
			union([int(lst[1]),int(lst[2])],[int(lst[3]),int(lst[4])])
			
		elif lst[0]=="UNMERGE":
			new_p=find([int(lst[1]),int(lst[2])],parents)
			for i in range(1,51):
				for j in range(1,51):
					if find([i,j],parents)==new_p:
						parents[i][j]=[i,j]
						if i==int(lst[1]) and j==int(lst[2]): continue
						else:
							values[i][j]=0
						


		else: #print
			if values[int(lst[1])][int(lst[2])]==0: answer.append("EMPTY")
			else: answer.append(values[int(lst[1])][int(lst[2])])


	return answer
