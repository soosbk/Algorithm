
def find(parent,a):
	if parent[a]!=a: parent[a]=find(parent,parent[a])
	return parent[a]

def union(parent,a,b):
	a=find(parent,a)
	b=find(parent,b)

	if a<b: parent[b]=a
	else: parent[a]=b




n,m=map(int,input().split())
q=[]
for _ in range(m):
	x,y,d=map(int,input().split())
	q.append([d,(x,y)])
q.sort()

parent=[x for x in range(n+1)]
	
answer=0
for i in q:
	distance,a=i
	if find(parent,a[0])!=find(parent,a[1]):
		union(parent,a[0],a[1])
	else:
		answer+=distance

print(answer)
