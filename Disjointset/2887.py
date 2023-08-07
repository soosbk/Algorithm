
def find(parent,a):
	if parent[a]!=a: parent[a]=find(parent,parent[a])
	return parent[a]

def union(parent,a,b):
	a=find(parent,a)
	b=find(parent,b)

	if a<b: parent[b]=a
	else: parent[a]=b




n=int(input())
x=[]
y=[]
z=[]
for i in range(1,n+1):
	data=list(map(int,input().split()))
	x.append((data[0],i))
	y.append((data[1],i))
	z.append((data[2],i))


x.sort()
y.sort()
z.sort()

planet=[]
parent=[x for x in range(n+1)]

for i in range(n-1):
	planet.append((x[i+1][0]-x[i][0],x[i][1],x[i+1][1]))
	planet.append((y[i+1][0]-y[i][0],y[i][1],y[i+1][1]))
	planet.append((z[i+1][0]-z[i][0],z[i][1],z[i+1][1]))

planet.sort()
answer=0
for i in planet:
	d,a,b=i
	if find(parent,a)!=find(parent,b):
		answer+=d
		union(parent,a,b)


print(answer)
