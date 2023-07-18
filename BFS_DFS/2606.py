n=int(input())
m=int(input())
li=[]
checklist=[False for i in range(0,n)]
for i in range(0,m):
	input_list=input().split(" ")
	li.append([int(input_list[0]),int(input_list[1])])
	
li=sorted(li,key=lambda x:(x[0],x[1]))

#DFS
cnt=0
stack=[]
stack.append(1)
while True:
	if len(stack)==0: 
		break
	f=stack[-1]
	del(stack[-1])
	if checklist[f-1]==True: continue
	checklist[f-1]=True
	cnt+=1
	for i in range(m-1,-1,-1):

		if (li[i][0]==f) and (checklist[li[i][1]-1]==False):
			stack.append(li[i][1])
			
		elif (li[i][1]==f) and (checklist[li[i][0]-1]==False):
			stack.append(li[i][0])
			
		
print(cnt-1)
