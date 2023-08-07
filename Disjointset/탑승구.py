def find(parent,a):
	if parent[a]!=a: parent[a]=find(parent,parent[a])
	return parent[a]

def union(parent,a,b):
	a=find(parent,a)
	b=find(parent,b)

	if a<b: parent[b]=a
	else: parent[a]=b



g=int(input())
p=int(input())
parent=[x for x in range(g+1)]
answer=0
for i in range(p):
	pa=find(parent,int(input()))
	if pa==0: break
	else: 
		union(parent,pa,pa-1)
		answer+=1
print(answer)



	

