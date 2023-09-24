t=int(input())

for _ in range(t):
	n=int(input())
	lst=[]
	for _ in range(n):
		lst.append(list(map(int,input().split())))

	lst.sort(reverse=True)
	stack=[]
	time=0
	for i in range(n):
		if len(stack)==0:
			stack.append(i)
			continue
		while stack and lst[stack[-1]][1]>lst[i][1]:
			time+=1
			stack.pop()
		stack.append(i)
	print(len(stack))
