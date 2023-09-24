n=int(input())
lst=[]
for _ in range(n):
	lst.append(list(map(int,input().split())))
answer=[]
lst=sorted(lst,key=lambda x:(x[1],x[0]))
i=0
for i in range(n):
	if len(answer)==0:
		answer.append(lst[i])
		continue

	if lst[i][0]<answer[-1][1]<=lst[i][1]:
		continue
	else:
		answer.append(lst[i])
print(len(answer))
