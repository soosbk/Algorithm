stream=input()
stack=[]
answer=0
for i in range(len(stream)):
	if stream[i]=="(":
		stack.append(i)

	else:
		idx=stack.pop()
		if i-idx==1:
			answer+=(len(stack))
			
		else:
			answer+=1


print(answer)
