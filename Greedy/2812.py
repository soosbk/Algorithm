n,k=map(int,input().split())
number=input()
stack=[]

for i in range(n):
	if len(stack)==0 or k==0:
		stack.append(number[i])
		continue
	while stack and stack[-1]<number[i] and k>0: #앞에서 수가 빠지는 것이 훨신 유리 -> 뒤로 갈 수록 10의 제곱 단위씩 늘어나는 거니까	
		k-=1
		stack.pop()
	stack.append(number[i])

if k>0:
	stack=stack[:-k]

print("".join(stack))
