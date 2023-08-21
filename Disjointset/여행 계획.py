

def find(parent,a):
	if parent[a]!=a:
		parent[a]=find(parent,parent[a])
	return parent[a]

def union(parent,a,b):
	a=find(parent,a)
	b=find(parent,b)


	if a>b:
		parent[a]=b
	else:
		parent[b]=a


n,m=map(int,input().split())





parent=[i for i in range(n+1)]

for i in range(n):
	data=list(map(int,input().split()))
	for j in range(n):
		if data[j]==1:
			union(parent,i+1,j+1)
plan=list(map(int,input().split()))


success=True
for i in range(1,len(plan)):
	if find(parent,plan[i-1])!=find(parent,plan[i]):
		success=False
		break

if success:
	print("YES")
else:
	print("NO")




