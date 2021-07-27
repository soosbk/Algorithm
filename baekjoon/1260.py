input_list=input().split(" ")
n=int(input_list[0])
m=int(input_list[1])
v=int(input_list[2])
li=[]
checklist=[False for i in range(0,n)]
for i in range(0,m):
	input_list=input().split(" ")
	li.append([int(input_list[0]),int(input_list[1])])
	
li=sorted(li,key=lambda x:(x[0],x[1]))


#DFS

checklist=[False for i in range(0,n)]

stack=[]
stack.append(v)
while True:
	#print(queue)
	if len(stack)==0: 
		break
	f=stack[-1]
	del(stack[-1])
	if checklist[f-1]==True: continue
	checklist[f-1]=True
	print(f,end=" ")
	for i in range(m-1,-1,-1):

		if (li[i][0]==f) and (checklist[li[i][1]-1]==False):
			stack.append(li[i][1])
			
		elif (li[i][1]==f) and (checklist[li[i][0]-1]==False):
			stack.append(li[i][0])
			
		
print()

#BFS
queue=[]
checklist=[False for i in range(0,n)]

plist=[]
queue.append(v)
checklist[v-1]=True
while True:
	plist.clear()
	for i in range(0,len(li)):
		if (queue[0]==li[i][1]) and (li[i][0] not in plist) and (checklist[li[i][0]-1]!=True) and (li[i][0] not in queue):
			plist.append(li[i][0])

		elif (queue[0]==li[i][0]) and (li[i][1] not in plist) and (checklist[li[i][1]-1]!=True) and (li[i][1] not in queue):
			plist.append(li[i][1])

	if len(plist)!=0: plist.sort()
	queue=queue+plist
	
	checklist[queue[0]-1]=True
	print(queue[0],end=" ")
	del(queue[0])
	if len(queue)==0: break



print()


