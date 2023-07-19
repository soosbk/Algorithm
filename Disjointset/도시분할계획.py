

def union(parent,a,b):
	a=find_parent(parent,a)
	b=find_parent(parent,b)
	if a<b:
		parent[b]=a
	else:
		parent[a]=b

def find_parent(parent,a):
	if parent[a]!=a:
		parent[a]= find_parent(parent,parent[a])
	return parent[a]



def check(parent,a,b):
	a=find_parent(parent,a)
	b=find_parent(parent,b)





n,m=map(int,input().split())
parent=[i for i in range(n+1)]

edges=[]
last=0
for i in range(m):
	a,b,c=map(int,input().split())
	edges.append((c,a,b))

edges.sort()

cost=0
for edge in edges:
	c,a,b=edge
	if find_parent(parent,a)!=find_parent(parent,b): 
		union(parent,a,b)
		cost+=c
		last=c #정렬했으니까 마지막이 가장 큰 길이의 간선
print(parent)

print(cost-last)



