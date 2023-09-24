n=int(input())
lst=list(map(int,input().split()))
answer=[-1]*n
stack=[]

for i in range(n):
	while stack and lst[stack[-1]]<lst[i]:
		print(stack)
		answer[stack.pop()]=lst[i]
	stack.append(i)



for i in range(n):
    print(answer[i],end=" ")
