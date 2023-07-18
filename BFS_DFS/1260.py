import sys
sys.setrecursionlimit(10**5)

n,m,v = map(int,input().split())
li={}

for i in range(0,m):
	input_list=input().split(" ")
	if int(input_list[0]) not in li: li[int(input_list[0])]=[int(input_list[1])]
	else: li[int(input_list[0])].append(int(input_list[1]))

	if int(input_list[1]) not in li: li[int(input_list[1])]=[int(input_list[0])]
	else: li[int(input_list[1])].append(int(input_list[0]))

for key in li:
	li[key].sort()



#DFS
checklist=[]

def dfs(edge):
	if edge not in li: return 
	
	k=list(li[edge])
	for i in range(0,len(k)):
		if str(k[i]) not in checklist: 
			checklist.append(str(k[i]))
			dfs(k[i])
			
		
checklist.append(str(v))
dfs(v)

print(" ".join(checklist))
	
			

#BFS
checklist2=[]
plist=[]
def bfs(edge):
	if edge not in li: 
		if len(checklist2)>1: 
			bfs(int(checklist2[1]))
		else: return 
	k=list(li[edge])
	for i in range(0,len(k)):
		if (str(k[i]) not in plist) and (str(k[i]) not in checklist2):
			checklist2.append(str(k[i]))
			plist.append(str(k[i]))
	
	if len(checklist2)>0:
		a=checklist2[0] 
		del(checklist2[0])
		bfs(int(a))


	



checklist2.append(str(v))
plist.append(str(v))
bfs(v)
print(" ".join(plist))
	
	
