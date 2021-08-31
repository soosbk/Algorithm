n,k=map(int, input().split())



queue=[i for i in range(1,n+1)]
string="<"

count=0
while len(queue)>1:
	count+=1
	if count%k: queue.append(queue[0])	
	else: string+=str(queue[0])+', '
	del(queue[0])

string+=str(queue[0])+'>'

print(string)
