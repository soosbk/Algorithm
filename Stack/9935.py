stream=input()

a=input()
stack=[]

for i in stream:
	if len(a)==1 and a==i: 
		continue
	if len(stack)<len(a)-1: 
		stack.append(i)
		continue
	if i==a[-1]:
		if "".join(stack[-len(a)+1:])==a[:-1]:
			for _ in range(len(a)-1): stack.pop()
			continue
	stack.append(i)

answer="".join(stack)
if answer=="": print("FRULA")
else: print(answer)
